from django.db import models

# Create your models here.


class booking(models.Model):
    email = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=60)
    customer_address = models.CharField(max_length=200)
    service_address = models.CharField(max_length=200)
    brand = models.CharField(max_length=60)
    model = models.CharField(max_length=100)
    service_type = models.CharField(max_length=60)
    time_slot = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    objects = models.Manager()