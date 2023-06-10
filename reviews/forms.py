from django.forms import ModelForm, Textarea
from .models import Review


class ReviewForm(ModelForm):
    """
    Renders Product Review form
    """
    class Meta:
        model = Review
        fields = ('rating', 'comment')
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        """
        Adds class to the fields
        """
        super().__init__(*args, **kwargs)

        self.fields['rating'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = (
                'border-green rounded review-form')
