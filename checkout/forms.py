from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name')
    eircode = forms.CharField(label='Postcode (optional)', required=False)
    street_address1 = forms.CharField(label='Street Address 1')
    street_address2 = forms.CharField(
        label='Street Address 2 (optional)', required=False)
    county = forms.CharField(label='County (optional)', required=False)

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'eircode', 'county',
                  'country',)

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, removes auto-generated
        labels and sets autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
