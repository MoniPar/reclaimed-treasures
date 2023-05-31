from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Adds labels and classes, and sets autofocus on first field
        """
        super().__init__(*args, **kwargs)

        labels = {
            'default_full_name': 'Full Name',
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_eircode': 'Eircode',
            'default_county': 'County, State or Locality',
            'default_country': 'Country',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                label = f'{labels[field]} *'
            else:
                label = labels[field]
            self.fields[field].widget.attrs['label'] = label
            self.fields[field].widget.attrs['class'] = (
                'border-green rounded profile-form-input')
            self.fields[field].label = label + ':'
