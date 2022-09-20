from django.db import models

# Create your models here.
class contanctpage(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    type = models.CharField(max_length=100)
    mobileNumber= models.IntegerField()

    objects = models.Manager()