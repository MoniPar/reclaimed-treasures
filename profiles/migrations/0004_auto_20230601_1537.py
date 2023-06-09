# Generated by Django 3.2.18 on 2023-06-01 15:37

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_userprofile_default_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='County/State/Region'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_eircode',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Eircode'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_full_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_street_address1',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Street Address 1'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_street_address2',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Street Address 2'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_town_or_city',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Town/City'),
        ),
    ]
