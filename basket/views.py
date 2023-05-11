from django.shortcuts import render, redirect


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
