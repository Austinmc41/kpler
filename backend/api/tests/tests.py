# from django.test import TestCase

# # Create your tests here.
# class CreateNewVesselTest(TestCase):
#     """ Test module for inserting a new puppy """

#     def setUp(self):
#         self.valid_payload = {
#             'vessel_id': 11,
#             'received_time_utc': '2022-11-23T17:39:00Z',
#             'latitude': -9,
#             'longitude': -19
#         }
#         self.invalid_payload = {
#             'name': 11,
#             'received_time_utc': '2022-11-23T17:39:00Z',
#             'latitude': -9,
#             'longitude': 19
#         }

#     def test_create_invalid_vesssel(self):
#         response = client.post(
#             reverse('post'),
#             data=json.dumps(self.invalid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)