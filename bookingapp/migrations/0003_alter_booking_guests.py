# Generated by Django 3.2.18 on 2023-04-08 11:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0002_alter_booking_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guests',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),
        ),
    ]
