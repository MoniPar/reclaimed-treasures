from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Model for the User's Profile
    maintains default delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Name")
    default_email = models.EmailField(
        max_length=254, null=True, blank=True, verbose_name="Email")
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Phone")
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True,
        verbose_name="Street Address 1")
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True,
        verbose_name="Street Address 2")
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True, verbose_name="Town/City")
    default_eircode = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Eircode")
    default_county = models.CharField(
        max_length=80, null=True, blank=True,
        verbose_name="County/State/Region")
    default_country = CountryField(
        blank_label='Select country', null=True, blank=True,
        verbose_name="Country")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """
        Gets Email from User Model
        """
        if self.default_email == "":
            self.default_email = self.user.email

        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates/updates the User's Profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Saves profile for existing users
    instance.userprofile.save()
