from global_land_mask import globe
from rest_framework.serializers import ValidationError

# checks for valid longitude and latitude and makes sure coordinates are maritime coordinates

def vessel_validator(data):
    errors = {}
    # checking if latitude is valid
    if data['latitude'] < -90 or data['latitude'] > 90:
        errors['latitude'] = f"{data['latitude']}  is not a valid latitude because it is not between -90.00000 and 90.00000. Code: 4999"
        
    # checking if longitude is valid 
    if data['longitude'] < -180 or data['longitude'] > 180:
        errors['longitude'] = f"{data['longitude']} is not a valid longitude because it is not between -180.00000 and 180.00000. Code: 5000"
    
    # want valid latitude and longitude before checking if coordinate is a maritime coordinate
    try:
        is_ocean = globe.is_ocean(data['latitude'], data['longitude'])
        if not is_ocean:
            errors['geo_coordinate'] = f"({data['latitude']}, {data['longitude']}) is a land coordinate. Please enter a maritime coordinate. Code: 5002"
    except Exception as e:
        errors['geo_coordinate'] = 'Cannot validate if maritime coordinate because coordinate is invalid: check latitude and longitude.'



    # @todo: check feasibility of travel distance over a particular time span
    
    
    # return dictionary of errors if there has been bad input field
    if errors:
        raise ValidationError(errors)
    return data