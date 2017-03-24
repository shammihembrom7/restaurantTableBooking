from __future__ import unicode_literals

from django.db import models
from restaurants.models import Restaurant

# Create your models here.

class Table(models.Model):
    capacity = models.IntegerField()
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)

    def __unicode__(self):
        tname = self.restaurant.name +" "+ str(self.capacity)+ " chairs"
        return tname

    def __str__(self):
        tname = self.restaurant.name +" "+ str(self.capacity)+ " chairs"
        return tname
