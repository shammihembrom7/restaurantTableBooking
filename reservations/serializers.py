from rest_framework import serializers

from reservations.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ('customer', 'table', 'booking', 'duration')
