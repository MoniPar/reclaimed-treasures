from django.db import models


class Category(models.Model):
    """
    Model for product categories
    """
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def __get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model for each of the products
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    theme = models.CharField(max_length=254)
    description = models.TextField()
    additional_information = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    available = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
