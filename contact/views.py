from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact(request):
    """
    Renders contact form
    """
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Your message was submitted successfully!")
            return redirect('/contact?submitted=True')
        else:
            # form = ContactForm()
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
