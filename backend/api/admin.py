from django.contrib import admin
from .models import Vessel

class VesselAdmin(admin.ModelAdmin):
    list_display = ('vessel_id', 'received_time_utc', 'latitude','longitude')
# Register your models here.

admin.site.register(Vessel, VesselAdmin)