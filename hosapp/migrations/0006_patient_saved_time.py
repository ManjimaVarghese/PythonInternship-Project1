# Generated by Django 4.2.7 on 2023-12-02 13:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0005_doctor_saved_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='saved_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
