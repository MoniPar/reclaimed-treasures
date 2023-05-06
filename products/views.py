from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    A view to show individual product details
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)
