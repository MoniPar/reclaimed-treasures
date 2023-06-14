from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact Model form
    """
    class Meta:
        model = Contact
        fields = (
            'subject', 'full_name', 'email', 'phone', 'message',
        )

    def __init__(self, *args, **kwargs):
        """
        Add class to fields
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = (
                'border-green rounded contact-form-input')
