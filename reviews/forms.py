from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Renders Product Review form
    """
    class Meta:
        model = Review
        fields = ('comment', 'rating')
