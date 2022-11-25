from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import VesselSerializer
from .models import Vessel
from django.views import View

# Create your views here.
# to get all quote
class VesselView(viewsets.ModelViewSet):
    serializer_class = VesselSerializer
    queryset = Vessel.objects.all()