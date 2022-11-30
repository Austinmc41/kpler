from django.contrib import admin
from .models import Vessel
# creating and registering Vessels in admin page
class VesselAdmin(admin.ModelAdmin):
    list_display = ('vessel_id', 'received_time_utc', 'latitude','longitude')


admin.site.register(Vessel, VesselAdmin)