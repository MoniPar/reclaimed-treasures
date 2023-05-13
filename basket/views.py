from django.shortcuts import render, redirect, reverse, HttpResponse


def shopping_basket(request):
    """
    Renders the shopping basket page
    """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Adds quantity of the specific chosen product to the shopping basket
    """
    # Get the quantity and the redirect_url from the form
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # Access the session if it exists and create it if it doesn't
    basket = request.session.get('basket', {})

    # Add item to the basket or update its quantity if already exists
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    # Override the variable in the session with the updated version
    request.session['basket'] = basket
    # print(request.session['basket'])
    return redirect(redirect_url)


def update_basket(request, item_id):
    """
    Updates the quantity of specific products to the specified amount
    """
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('shopping_basket'))


def remove_from_basket(request, item_id):
    """
    Removes a specified product from the shopping basket
    """
    try:
        basket = request.session.get('basket', {})

        basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
