from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=30,default="Your name")
    job = models.CharField(max_length=30, default="your Job")