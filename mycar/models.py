from django.db import models

# Create your models here.


class mycar(models.Model):
    email = models.CharField(max_length=50)
    brand = models.CharField(max_length=60)
    model_Name = models.CharField(max_length=60)
    vehicle_number = models.CharField(max_length=60)
    year_Of_Model = models.IntegerField(null=True)
    fuel_Type = models.CharField(max_length=20)
    mobile_number = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    objects = models.Manager()