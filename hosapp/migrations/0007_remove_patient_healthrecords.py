# Generated by Django 4.2.7 on 2023-12-03 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0006_patient_saved_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='healthrecords',
        ),
    ]