from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name', 'name'
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'sku', 'name', 'category', 'price',
        'stock', 'available', 'image', 'img_thumbnail',
    )

    ordering = ('sku',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
