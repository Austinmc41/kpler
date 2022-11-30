from django.test import TestCase
from ..models import Vessel
from django.db import models
from datetime import datetime
import dateutil
from dateutil.parser import parse

class VesselTest(TestCase):


    def setUp(self):
        Vessel.objects.create(
            vessel_id=11,
            received_time_utc= datetime(2021, 3, 4, 14, 57, 11, tzinfo=dateutil.tz.tz.tzutc()),
            latitude= -9,
            longitude= -19)

    def test_vessel(self):
        vessel_eleven = Vessel.objects.get(vessel_id=11)
        self.assertEqual(
            vessel_eleven.get_vessel_id(), 11)
        self.assertEqual(
            vessel_eleven.get_received_time_utc(), datetime(2021, 3, 4, 14, 57, 11,tzinfo=dateutil.tz.tz.tzutc()))
        self.assertEqual(
            vessel_eleven.get_latitude(), -9)
        self.assertEqual(
            vessel_eleven.get_longitude(), -19)
