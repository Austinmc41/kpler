from django.db import models

# Create your models here.

class Vessel(models.Model):
    vessel_id =  models.IntegerField()
    received_time = models.DateTimeField() 
    latitude = models.FloatField()
    longitude = models.FloatField()

    def _str_(self):
        return self.title

