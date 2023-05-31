from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Represents the User Profile Model in the Admin interface
    """
    fields = ('default_full_name', 'default_email', 'default_phone_number',
              'default_street_address1', 'default_street_address2',
              'default_town_or_city', 'default_eircode', 'default_county',
              'default_country')

    list_display = ('default_full_name', 'default_email',
                    'default_phone_number', 'default_country')
