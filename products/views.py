from django.shortcuts import render
from .models import Product


def shop(request):
    """
    A view to show all products
    """
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'products/shop.html', context)
