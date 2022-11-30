import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Vessel
from ..serializers import VesselSerializer
import dateutil
from datetime import datetime


# initialize the APIClient app
client = Client()


class GetAllVessels(TestCase):
    """ Test module for GET all Vessels API """

    def setUp(self):
        Vessel.objects.create(
            vessel_id=10,
            received_time_utc= datetime(2020, 3, 4, 14, 57, 11, tzinfo=dateutil.tz.tz.tzutc()),
            latitude= -9,
            longitude= -19)
        Vessel.objects.create(
            vessel_id=11,
            received_time_utc= datetime(2021, 3, 4, 14, 57, 11, tzinfo=dateutil.tz.tz.tzutc()),
            latitude= -9,
            longitude= -19)
        Vessel.objects.create(
            vessel_id=12,
            received_time_utc= datetime(2022, 3, 4, 14, 57, 11, tzinfo=dateutil.tz.tz.tzutc()),
            latitude= -9,
            longitude= -19)
        Vessel.objects.create(
            vessel_id=13,
            received_time_utc= datetime(2019, 3, 4, 14, 57, 11, tzinfo=dateutil.tz.tz.tzutc()),
            latitude= -9,
            longitude= -19)

    def test_get_all_vessels(self):
       # get API response
        response = client.get(reverse('vessels'))
        # get data from db
        vessels = Vessel.objects.all()
        serializer = VesselSerializer(vessels, many=True)
        self.assertEqual(response.data['payload'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)