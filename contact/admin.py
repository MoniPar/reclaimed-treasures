from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Displays the Contact Model in the Admin interface
    """
    readonly_fields = (
        'full_name', 'email', 'phone', 'message', 'submitted_on'
    )

    fields = (
        'subject', 'full_name', 'email', 'phone', 'message',
        'submitted_on', 'actioned',
    )

    list_display = (
        'subject', 'full_name', 'email', 'submitted_on', 'actioned',
    )

    ordering = ('-submitted_on',)


admin.site.register(Contact, ContactAdmin)
