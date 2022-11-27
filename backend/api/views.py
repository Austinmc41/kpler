from django.shortcuts import render
from rest_framework import  status
from .serializers import VesselSerializer
from .models import Vessel
from rest_framework.views import APIView
from rest_framework.response import Response




# Create your views here.

class VesselView(APIView):
    serializer_class = VesselSerializer
    
    # handle get Vessel positions
    def get(self, request, *args, **kwargs):
        vessel_objects = Vessel.objects.all()
        serializer = VesselSerializer(vessel_objects, many=True)
        return Response({'status' : 200, 'payload': serializer.data})

    # handle create vessel position 
    # @todo: in the future handle things bulk csv import and JSON list inputs
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status' : 200, 'payload': serializer.data})
        else:
            return Response({'status' : 400, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
           

    
