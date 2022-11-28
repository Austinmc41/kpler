from django.db import models
from django.core.exceptions import ValidationError


class Vessel(models.Model):
    vessel_id =  models.IntegerField()
    received_time_utc = models.DateTimeField() 
    latitude = models.FloatField()
    longitude = models.FloatField()

    def _str_(self):
        return self.title

