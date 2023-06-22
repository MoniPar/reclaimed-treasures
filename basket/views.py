from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def shopping_basket(request):
    """
    Renders the shopping basket page
    """
    context = {
        'on_basket_page': True
    }
    return render(request, 'basket/basket.html', context)


def add_to_basket(request, item_id):
    """
    Adds quantity of the specific chosen product to the shopping basket
    """
    product = get_object_or_404(Product, pk=item_id)
    # Get the quantity and the redirect_url from the form
    quantity = int(request.POST.get('quantity') or 0)
    redirect_url = request.POST.get('redirect_url')
    # Access the session if it exists and create it if it doesn't
    basket = request.session.get('basket', {})

    # Update quantity of product in basket or add it
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request,
                         f'You now have {basket[item_id]} of {product.name}'
                         ' in your basket.')
    else:
        basket[item_id] = quantity
        messages.success(request,
                         f'{product.name} has been added to your basket!')

    # Override the variable in the session with the updated version
    request.session['basket'] = basket
    # print(request.session['basket'])
    return redirect(redirect_url)


def update_basket(request, item_id):
    """
    Updates the quantity of specific products to the specified amount
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity') or 0)
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request,
                         f'You now have {basket[item_id]} of {product.name}'
                         ' in your basket')
    else:
        basket.pop(item_id)
        messages.success(request,
                         f'{product.name} has been removed from your basket!')

    request.session['basket'] = basket
    return redirect(reverse('shopping_basket'))


def remove_from_basket(request, item_id):
    """
    Removes a specified product from the shopping basket
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(request,
                         f'{product.name} was successfully removed'
                         ' from your basket!')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
