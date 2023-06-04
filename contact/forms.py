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
        Add custom labels & set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['subject'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = (
                'border-green rounded contact-form-input')
