from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from basket.contexts import basket_contents
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Adds the save info box to the metadata key of the payment intent
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request,
                       "Sorry, your payment cannot be processed"
                       " right now. Please try again later.")
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Gets session data and checks form validation
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'eircode': request.POST['eircode'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            checked_products = []

            # Iterates through the products in the basket, checking quantity
            # against product stock and saving each checked product in a list
            for item_id, quantity in basket.items():
                product = Product.objects.get(id=item_id)
                # If there's stock
                if product.stock > 0:
                    # and quantity ordered is less than the no. in stock
                    if quantity < product.stock:
                        # set to deduct the quantity ordered from the stock
                        product.stock -= quantity
                        checked_products.append((product, quantity))
                    # If quantity ordered is greater than the no. in stock
                    elif quantity > product.stock:
                        # and greater than the overflow of 3, redirect back to
                        # the shopping basket
                        if (quantity - product.stock) > 3:
                            messages.warning(request,
                                             f"There's only { product.stock } "
                                             f"of { product.name } left in "
                                             "stock! If you like, we can make "
                                             "up to 3 of this product to "
                                             "order. Please adjust your "
                                             "quantity to stay within this "
                                             "limit.")

                            return redirect(reverse('shopping_basket'))
                        # If quantity ordered is less than the overflow of 3
                        else:
                            messages.info(request,
                                          f"There's only { product.stock } of "
                                          f"{ product.name } left in stock! We"
                                          " will make the overflow to order. "
                                          "Please be aware that they will take"
                                          " between 3 to 5 extra days to "
                                          "deliver!")
                            # sets the product stock to 0
                            product.stock = 0
                            checked_products.append((product, quantity))
                    # If quantity ordered is equal to the no. in stock
                    else:
                        # sets stock to 0
                        product.stock = 0
                        checked_products.append((product, quantity))
                # If there's no stock i.e. product is made to order
                else:
                    messages.info(request,
                                  f"{ product.name } is currently out of "
                                  "stock and will be made to order. "
                                  "Please be aware that it will take "
                                  "3 to 5 extra days to deliver!")
                    checked_products.append((product, quantity))

            # Iterates through the list of checked products, saves the
            # difference in stock in the database and creates each line item
            for product, quantity in checked_products:
                product.save()
                try:
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request,
                                   "One of the products in your basket "
                                   "wasn't found in the database. Please "
                                   "call us for further assistance!")
                    order.delete()
                    return redirect(reverse('shopping_basket'))

            # Saves the information to the user's profile
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        # If form is not valid
        else:
            messages.error(request,
                           "There was an error  with your form. "
                           "Please check your information again!")
            return redirect(reverse('checkout'))
    # If request is GET
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "You don't have anything in your basket!")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempts to prefill the form with User's Profile info
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                # Uses initial parameter on order form to prefill all fields
                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.default_email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'eircode': profile.default_eircode,
                    'county': profile.default_county,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                # Renders an empty form
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request,
                         "The Stripe public key is missing. "
                         "Did you forget to set it in your environment?")

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handles successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attaches the user's profile to the order
        order.user_profile = profile
        order.save()

        # Saves the user's info
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default.email': order.email,
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_eircode': order.eircode,
                'default_county': order.county,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request,
                     "Order successfully processed! Your order number is "
                     f"{order_number}. A confirmation email will be sent "
                     f"to {order.email}.")
    # Deletes the user's basket from the session once the order is complete
    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
