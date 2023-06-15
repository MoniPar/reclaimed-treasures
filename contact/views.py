from django.shortcuts import render, redirect
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
            subject = form.cleaned_data['subject'],
            body = {
                'name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            connect = get_connection(settings.EMAIL_BACKEND)
            email_to = settings.DEFAULT_FROM_EMAIL,
            email_from = 'email'
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
