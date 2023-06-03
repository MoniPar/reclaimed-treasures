from django.shortcuts import render
from . models import Contact


def contact(request):
    """
    Renders contact form
    """
    return render(request, 'contact/contact.html')
