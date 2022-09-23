from django.db import models

# Create your models here.
class contanctpage(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    type = models.CharField(max_length=100)
    mobileNumber= models.IntegerField()

    objects = models.Manager()


class cars(models.Model):
    brand = models.CharField(max_length=60)
    model_name =  models.CharField(max_length=60)

    objects = models.Manager()


class mycar(models.Model):
    email = models.CharField(max_length=50)
    brand = models.CharField(max_length=60)
    model_Name = models.CharField(max_length=60)
    vehicle_number = models.CharField(max_length=60)
    year_Of_Model = models.IntegerField(null=True)
    fuel_Type = models.CharField(max_length=20)
    mobile_number = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    objects = models.Manager()