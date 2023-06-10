from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from products.models import Product
from .models import Review
from .forms import ReviewForm


def list_reviews(request, product_id):
    """
    View for displaying product reviews
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.all()
    # form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        # 'form': form,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_review(request, product_id):
    """
    View for handling review form
    """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.rating = form.cleaned_data['rating']
            review.comment = form.cleaned_data['comment']
            review.product = product
            review.rated_by = request.user
            review.save()
            messages.success(request, "Thank you, your review has been "
                                      "submitted!")
            return redirect(reverse('products'))
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'review': review,
    }

    return render(request, 'products/product_detail.html', context)
