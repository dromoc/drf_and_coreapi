from django.db import models

# Create your models here.


class Company(models.Model):
    address = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    site = models.URLField()
