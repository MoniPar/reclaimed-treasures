# Generated by Django 3.2.18 on 2023-05-31 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20230531_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
