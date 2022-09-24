from django.db import models

# Create your models here.
class contanctpage(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    type = models.CharField(max_length=100)
    mobileNumber = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    objects = models.Manager()