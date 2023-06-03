from django.db import models


class Contact(models.Model):
    """
    Model for Contact Form
    """
    SUBJECT_CHOICES = [
        ('', 'Choose Query Subject'),
        ('PRODUCT', 'Product Query'),
        ('ORDER', 'Order Query'),
        ('COMMISSION', 'Commission Query'),
        ('FEEDBACK', 'Feedback'),
        ('OTHER', 'Other'),
    ]

    subject = models.CharField(
        max_length=50, choices=SUBJECT_CHOICES, default='')
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=16, null=True, blank=True)
    message = models.TextField(max_length=2000)
    submitted_on = models.DateTimeField(auto_now_add=True)
    actioned = models.BooleanField(default=False)

    def __str__(self):
        return self.email
