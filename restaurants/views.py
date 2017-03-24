from django.shortcuts import render_to_response
from rest_framework import viewsets
from rest_framework import filters

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_fields = ('name', 'cuisine', 'location')
