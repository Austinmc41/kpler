from django.db import models
from django.core.exceptions import ValidationError

# creating Vessel object in data base 
class Vessel(models.Model):
    vessel_id =  models.IntegerField()
    received_time_utc = models.DateTimeField() 
    latitude = models.FloatField()
    longitude = models.FloatField()
    # boiler plate getters and setters 
    def get_vessel_id(self):
        return self.vessel_id
    
    def get_received_time_utc(self):
        return self.received_time_utc

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def _str_(self):
        return self.title

