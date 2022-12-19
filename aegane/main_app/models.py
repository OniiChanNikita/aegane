from django.db import models

# Create your models here.

class ProfileUser(models.Model):
    username = models.CharField(max_length=100)
    logo_user = models.ImageField(default='')