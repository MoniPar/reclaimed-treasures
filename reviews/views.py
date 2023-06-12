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

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_review(request, product_id):
    """
    View for handling add review form
    """
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm()
    review = []
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
            return redirect(reverse('product_detail', args=[product_id]))
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'form': form,
        'review': review,
    }

    return render(request, 'reviews/add_review.html', context)


@login_required
def edit_review(request, review_id):
    """
    View for handling edit review form
    """
    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    if review.rated_by != request.user:
        messages.error(request, "Sorry, you are not authorised to edit"
                       " this review!")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been successfully "
                                      "updated|")
            return redirect(reverse('product_detail', args=[product.id]))

        else:
            messages.error(request, "Failed to update review. Please make "
                                    "sure both fields are filled in and try "
                                    "again.")
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'review': review,
        'product': product,
    }

    return render(request, 'reviews/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """
    View to handle review deletion
    """
    review = get_object_or_404(Review, pk=review_id)
    product = review.product

    if request.method == 'POST':

        if request.user == review.rated_by:
            review.delete()
            messages.success(request, 'Your review has been deleted!')

            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Sorry, you are not authorised to delete "
                                    "this review!")

            return redirect(reverse('home'))

    context = {
        'review': review,
        'product': product,
    }

    return render(request, 'reviews/confirm_delete_review.html', context)
