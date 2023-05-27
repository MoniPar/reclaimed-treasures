from django.shortcuts import render
from .models import UserProfile


def profile(request):
    """
    Displays the User Profile
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
