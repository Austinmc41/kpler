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
        is_many = isinstance(request.data, list)

        # handles request with list of json objects else takes individual string
        if is_many:
            response = []
            for vessel in self.request.data:
                serializer = self.serializer_class(data=vessel)

                if serializer.is_valid():
                    serializer.save()
                    response.append({'status' : 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
                else:
                    response.append({'status' : 400, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status' : 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status' : 400, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        
        return Response(response, status=status.HTTP_201_CREATED)
           

    
