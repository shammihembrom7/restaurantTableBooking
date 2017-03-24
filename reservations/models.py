from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from restaurants.models import Restaurant
from customers.models import Customer
# Create your models here.

class Reservation(models.Model):
    table = models.ForeignKey('tables.Table', on_delete=models.CASCADE)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    booking = models.DateTimeField()
    duration = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __unicode__(self):
        return self.customer.name

    def __str__(self):
        return self.customer.name
