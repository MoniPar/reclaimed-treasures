from django.forms import ModelForm, Textarea
from .models import Contact


class ContactForm(ModelForm):
    """
    Contact Model form
    """
    class Meta:
        model = Contact
        fields = (
            'subject', 'full_name', 'email', 'phone', 'message',
        )
        widgets = {
            'message': Textarea(attrs={'cols': 40, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        """
        Adds class to fields
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = (
                'border-green rounded contact-form-input')
