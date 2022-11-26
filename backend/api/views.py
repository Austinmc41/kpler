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
        print("Here")
    

        # vessel_id = request.data['vessel_id']
        # recieved = request.data['received_time']
        # latitude = request.data['latitude']
        # longitude = request.data['longitude']

        
        # res = self.valid_coords(latitude, longitude)
        
        # if res:
        #     return res

        

        serializer = self.serializer_class(data=request.data)
        # serializer.valid_latitude(latitude) 
        # serializer.valid_longitude(longitude)

        if serializer.is_valid():
            serializer.save()
            return Response({'status' : 200, 'payload': serializer.data})
        else:
            return Response({'status' : 400, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
           

    

    # def validate_coords(self, latitude, longitude):

    #     if latitude < -90 or latitude > 90:
    #         return Response({'Message': str(latitude) + " is not a valid latitude because it is not between -90.00000 and 90.00000."}, status=status.HTTP_400_BAD_REQUEST)

    #     if longitude < -180 or latitude > 180:
    #         return Response({'Message': str(longitude) + " is not a valid longitude because it is not between -180.00000 and 180.00000."},  status=status.HTTP_400_BAD_REQUEST)
            
    #     is_in_ocean = globe.is_ocean(latitude, longitude)

        # if not is_in_ocean:
        #     return Response({'Message': '(' + str(latitude) + ', ' + str(longitude) + ')' + ' is a land coordinate. \
        #     Please enter a maritime coordinate.'},  status=status.HTTP_400_BAD_REQUEST)
