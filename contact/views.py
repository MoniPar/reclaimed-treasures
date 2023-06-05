from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, get_connection
from django.conf import settings
from .models import Contact
from .forms import ContactForm


# Code adapted from https://www.youtube.com/watch?v=1ihn3iRXtsY
def contact(request):
    """
    Handles the Contact Form display, submission and sends email to
    business address.
    """
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form_cleaned = form.cleaned_data
            form.save()
            connect = get_connection(settings.EMAIL_BACKEND)
            email_to = settings.DEFAULT_FROM_EMAIL,
            email_from = form_cleaned['email']
            send_mail(
                form_cleaned['subject'],
                form_cleaned['message'],
                email_from,
                email_to,
                connection=connect
            )
            messages.success(request,
                             "Your message was submitted successfully!")
            return redirect('/contact?submitted=True')
        else:
            messages.error(request,
                           "There was an error while submitting your "
                           "message.  Please make sure all required fields "
                           "are filled in correctly and try again.")
            return redirect('/contact')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted
    }

    return render(request, 'contact/contact.html', context)
