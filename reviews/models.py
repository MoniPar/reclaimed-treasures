from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Model for adding Product Reviews
    """
    RATING_CHOICES = (
        ('', '--'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    rated_by = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    rated_on = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=250)
    rating = models.IntegerField(choices=RATING_CHOICES, default='')

    def __str__(self):
        return f'{ self.product.name }'

    class Meta:
        unique_together = ('product', 'rated_by')
        ordering = ['-rated_on']
