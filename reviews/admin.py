from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Defines the model on the Admin Interface
    """
    list_display = (
        'product', 'rated_by', 'comment', 'rating', 'rated_on',
    )


admin.site.register(Review, ReviewAdmin)
