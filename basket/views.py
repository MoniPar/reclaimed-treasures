from django.shortcuts import render


def shopping_basket(request):
    """
    A view that renders the shopping basket page
    """

    return render(request, 'basket/basket.html')
