from django.shortcuts import render_to_response
from rest_framework import viewsets

from tables.models import Table
from tables.serializers import TableSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filter_fields=('__all__')
