from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'eircode', 'county',
                  'country',)

    def __init__(self, *args, **kwargs):
        """
        Adds classes, removes auto-generated
        labels and sets autofocus on first field
        """
        super().__init__(*args, **kwargs)

        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'eircode': 'Post Code',
            'county': 'County, State or Locality',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            label = labels[field]
            self.fields[field].label = label
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
