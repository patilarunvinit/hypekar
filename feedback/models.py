from django.db import models

# Create your models here.
class FeedBack(models.Model):
    email = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    rating = models.IntegerField()
    location = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)


    objects = models.Manager()