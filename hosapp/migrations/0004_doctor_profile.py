# Generated by Django 4.2.7 on 2023-12-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0003_remove_doctor_prescription_upload_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='profile',
            field=models.ImageField(default='', upload_to='profile'),
        ),
    ]