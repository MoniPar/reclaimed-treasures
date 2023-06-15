from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail, get_connection, BadHeaderError
from django.http import HttpResponse
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
            form.save()
            subject = request.POST.get('subject')
            body = {
                'message': form.cleaned_data['message'],
                'name': form.cleaned_data['full_name'],
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
            }
            # Joins the cleaned fields together to send as a message in email.
            # Filters out the None values from the iterable and converts other
            # values to strings. Credit: https://tinyurl.com/y9a993x9
            message = "\n".join(
                filter(
                    lambda x: str(x) if x is not None else '', body.values()))
            connect = get_connection(settings.EMAIL_BACKEND)
            email_to = settings.DEFAULT_FROM_EMAIL,
            email_from = form.cleaned_data['email']
            try:
                send_mail(
                    subject,
                    message,
                    email_from,
                    email_to,
                    connection=connect
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")

            messages.success(request, "Your message was submitted "
                                      "successfully!")
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
