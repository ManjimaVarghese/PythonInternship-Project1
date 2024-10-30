from django.db import models
from django.utils import timezone

class Patient(models.Model):

    name = models.CharField(max_length = 200)
    age = models.IntegerField(null = True)
    mobile = models.IntegerField(null = True)
    gender = models.CharField(max_length=10, null=True)
    disease = models.CharField(max_length=50, null=True)
    doctor = models.CharField(max_length=50, null=True)
   
    saved_time = models.DateTimeField(default=timezone.now)

class Doctor(models.Model):
    Dr_name = models.CharField(max_length = 200)
    Patient_name = models.CharField(max_length = 200)
    profile=models.ImageField(upload_to='profile',default="")
    saved_time = models.DateTimeField(default=timezone.now)

   