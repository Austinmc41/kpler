from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


# def valid_latitude(value):
#     if value < -90 or value > 90:
#         raise ValidationError(str(value) + " is not a valid latitude.")


# def valid_longitude(value):
#     if value < -180 or value > 180:
#         raise ValidationError(str(value) + " is not a valid longitude.")


class Vessel(models.Model):
    vessel_id =  models.IntegerField()
    received_time = models.DateTimeField() 
    latitude = models.FloatField()
    longitude = models.FloatField()

    def _str_(self):
        return self.title

