# Generated by Django 4.2.21 on 2025-05-14 21:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=5, validators=[django.core.validators.MaxValueValidator(100.0)]),
        ),
    ]
