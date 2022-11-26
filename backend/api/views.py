from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import VesselSerializer
from .models import Vessel
from rest_framework.views import APIView
from rest_framework.response import Response
from global_land_mask import globe
from numpy import *



# Create your views here.

class VesselView(APIView):
    serializer_class = VesselSerializer
    
    def get(self, request, *args, **kwargs):
        vessel_objects = Vessel.objects.all()
        serializer = VesselSerializer(vessel_objects, many=True)
        return Response({'status' : 200, 'payload': serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status' : 200, 'payload': serializer.data})
        else:
            return Response({'status' : 400, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
           

    
