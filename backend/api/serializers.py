from rest_framework import serializers
from .models import Vessel
from .validators import vessel_validator


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = ('vessel_id', 'received_time_utc', 'latitude','longitude')

    def validate(self, data):
        return vessel_validator(data)

    

    