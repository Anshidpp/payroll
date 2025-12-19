from django.db import models

# Create your models here.
class user(models.Model):
    Name =  models.CharField(max_length=100)
    Age = models.IntegerField(null=True,blank=True)
    Phone = models.CharField(max_length=10)
    Place = models.CharField(max_length=50)