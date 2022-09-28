from django.db import models

# Create your models here.
class cars(models.Model):
    brand = models.CharField(max_length=60)
    model_name =  models.CharField(max_length=60)
    basic =  models.IntegerField(null=True)
    standard =  models.IntegerField(null=True)
    premium =  models.IntegerField(null=True)

    objects = models.Manager()