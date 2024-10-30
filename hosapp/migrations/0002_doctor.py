# Generated by Django 4.2.7 on 2023-11-30 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dr_name', models.CharField(max_length=200)),
                ('Patient_name', models.CharField(max_length=200)),
                ('Prescription_upload', models.IntegerField(null=True)),
                ('profile', models.ImageField(default='', upload_to='profile')),
            ],
        ),
    ]