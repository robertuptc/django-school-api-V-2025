# Generated by Django 4.2.21 on 2025-05-14 21:45

from django.db import migrations, models
import subject_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('subject_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='professor',
            field=models.CharField(default='Professor.Cahan', max_length=255, validators=[subject_app.validators.validate_professor_format]),
        ),
    ]
