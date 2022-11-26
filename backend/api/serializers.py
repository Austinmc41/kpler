from rest_framework import serializers
from .models import Vessel
from global_land_mask import globe
from numpy import *


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = ('vessel_id', 'received_time', 'latitude','longitude')


    def validate(self, data):

        errors = {}

        # checking if latitude is valid
        if data['latitude'] < -90 or data['latitude'] > 90:
            errors['latitude'] = str(data['latitude']) + " is not a valid latitude because it is not between -90.00000 and 90.00000."
          
        # checking if longitude is valid 
        if data['longitude'] < -180 or data['longitude'] > 180:
            errors['longitude'] = str(data['longitude']) + " is not a valid longitude because it is not between -180.00000 and 180.00000."
        
        # want valid latitude and longitude before checking if coordinate is a maritime coordinate
        try:
            is_ocean = globe.is_ocean(data['latitude'], data['longitude'])
            if not is_ocean:
                errors['geo-coordinate'] = '(' + str(data['latitude']) + ', ' + str(data['longitude']) + ')'  + ' is a land coordinate. \
                Please enter a maritime coordinate.'
        except Exception as e:
            errors['geo-coordinate'] = 'Cannot validate if maritime coordinate because coordinate is invalid: check latitude and longitude.'



        # @todo: check feasibility of travel distance over a particular time span
        
        
        # return dictionary of errors if there has been bad input field
        if errors:
            raise serializers.ValidationError(errors)
        return data

    

    