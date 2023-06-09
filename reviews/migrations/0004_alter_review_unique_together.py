# Generated by Django 3.2.18 on 2023-06-21 08:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0003_auto_20230620_0927'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('product', 'rated_by')},
        ),
    ]
