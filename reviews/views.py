from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Review
from .forms import ReviewForm


def review_list(request):
    """
    View for displaying product reviews
    """
    reviews = Review.objects.all()
    form = ReviewForm()

    context = {
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'product_detail.html', context)
