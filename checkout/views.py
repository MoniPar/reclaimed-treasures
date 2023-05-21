from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from basket.contexts import basket_contents
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
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
        intent = stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        print(intent)
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
            order = order_form.save()
            # Iterates through the items in basket and creates each line item
            for item_id, quantity in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    # Decrements stock depending on quantity purchased
                    product.stock -= quantity
                    product.save()
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
            # Save the information to the user's profile
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
