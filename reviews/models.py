from __future__ import unicode_literals

from django.db import models
from customers.models import Customer
from restaurants.models import Restaurant

# Create your models here.

class Review(models.Model):
    review = models.CharField(max_length=400)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.review

    def __str__(self):
        return self.review
