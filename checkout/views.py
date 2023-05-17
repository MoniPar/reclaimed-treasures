from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """
    Gets session data and checks form validation
    """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "You don't have anything in your basket!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
