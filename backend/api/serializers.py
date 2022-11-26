from rest_framework import serializers
from .models import Vessel
from global_land_mask import globe
from numpy import *


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = ('vessel_id', 'received_time', 'latitude','longitude')


    def validate(self, data):

        if data['latitude'] < -90 or data['latitude'] > 90:
            raise serializers.ValidationError(str(data['latitude']) + " is not a valid latitude because it is not between -90.00000 and 90.00000.")
            
        if data['longitude'] < -180 or data['longitude'] > 180:
            raise serializers.ValidationError(str(data['longitude']) + " is not a valid longitude because it is not between -180.00000 and 180.00000.")

        if not globe.is_ocean(data['latitude'], data['longitude']):
            raise serializers.ValidationError('(' + str(data['latitude']) + ', ' + str(data['longitude']) + ')'  + ' is a land coordinate. \
            Please enter a maritime coordinate.') 

        return data

    

    