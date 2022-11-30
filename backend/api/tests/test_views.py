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
    # creating vessels 
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
    # getting all vessels
    def test_get_all_vessels(self):
       # get API response
        response = client.get(reverse('vessels'))
        # get data from db
        vessels = Vessel.objects.all()
        serializer = VesselSerializer(vessels, many=True)
        self.assertEqual(response.data['payload'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateVesselTest(TestCase):
    """ Test module for inserting a new puppy """
    
    def setUp(self):
        self.valid_payload = {
            'vessel_id': 11,
            'received_time_utc': '2022-11-23T17:39:00Z',
            'latitude': -9,
            'longitude': -19
        }
        self.invalid_maritime = {
            'vessel_id': 11,
            'received_time_utc': '2022-11-23T17:39:00Z',
            'latitude': -9,
            'longitude': 19
        }
        self.invalid_time_format = {
            'vessel_id': 11,
            'received_time_utc': '2022-11-23fefvfdT17:39:00Z',
            'latitude': -9,
            'longitude': -19
        }
        self.invalid_latitude = {
            'vessel_id': 11,
            'received_time_utc': '2022-11-23fefvfdT17:39:00Z',
            'latitude': -932432,
            'longitude': -19
        }
        self.invalid_longitude = {
            'vessel_id': 11,
            'received_time_utc': '2022-11-23fefvfdT17:39:00Z',
            'latitude': -9,
            'longitude': -1932432
        }

    def test_create_valid_vessel(self):
        response = client.post(
            reverse('vessels'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_maritime(self):
        response = client.post(
            reverse('vessels'),
            data=json.dumps(self.invalid_maritime),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_invalid_time_format(self):
        response = client.post(
            reverse('vessels'),
            data=json.dumps(self.invalid_time_format),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_invalid_latitude(self):
        response = client.post(
            reverse('vessels'),
            data=json.dumps(self.invalid_latitude),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_invalid_longitude(self):
        response = client.post(
            reverse('vessels'),
            data=json.dumps(self.invalid_longitude),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)