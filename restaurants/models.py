from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    cuisine = models.CharField(max_length=40)
    location = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
