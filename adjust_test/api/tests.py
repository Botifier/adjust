from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework.views import status

from .models import SampleDataSet


class SampleDataSetViewTest(APITestCase):
    API_URL = reverse('sample-data-set-list')
    # we always have value1 < value2 to make testing easier
    TEST_DATA = {
        'dates' : ['2018-01-01', '2019-09-09'],
        'channels' : ['channel1', 'channel2'],
        'countries' : ['country1', 'country2'],
        'os' : ['os1', 'os2'],
        'impressions' : [1, 2],
        'clicks': [3, 4],
        'installs': [5, 6],
        'spend' : [7.0, 8.0],
        'revenue' : [9.0, 10.0],
    }
    TOTAL_ENTRIES = 2**9
    
    def setUp(self):
        super().setUp()
        self._insert_test_data()

    def _insert_test_data(self):
        for date in self.TEST_DATA['dates']:
            for channel in self.TEST_DATA['channels']:
                for country in self.TEST_DATA['countries']:
                    for os in self.TEST_DATA['os']:
                        for impressions in self.TEST_DATA['impressions']:
                            for clicks in self.TEST_DATA['clicks']:
                                for installs in self.TEST_DATA['installs']:
                                    for spend in self.TEST_DATA['spend']:
                                        for revenue in self.TEST_DATA['revenue']:
                                            SampleDataSet.objects.create(
                                                date=date,
                                                channel=channel,
                                                country=country,
                                                os=os,
                                                impressions=impressions,
                                                clicks=clicks,
                                                installs=installs,
                                                spend=spend,
                                                revenue=revenue,
                                            )
                                            
    def test_field_selection(self):
        data = {
            'fields': 'country,channel',
        }
        response = self.client.get(self.API_URL, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.TOTAL_ENTRIES)
        for entry in response.data:
            self.assertEqual(set(entry.keys()), {'country', 'channel'})                                        

    def test_filtering(self):
        data = {
            'country': 'country1',
            'os': 'os1',
        }
        response = self.client.get(self.API_URL, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # we removed 2*2 multiplier of the possibities by excluding half the countries and half the os
        self.assertEqual(len(response.data), self.TOTAL_ENTRIES / 4)        
        for entry in response.data:
            self.assertEqual(entry['country'], 'country1')
            self.assertEqual(entry['os'], 'os1')
        
        # Test negative filter
        data = {
            'country': 'non_existing_country',
        }
        response = self.client.get(self.API_URL, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])       

    def test_sorting(self):
        data = {
            'ordering': 'date,-channel,-country,-os,-impressions,-clicks,installs,spend,revenue'
        }
        response = self.client.get(self.API_URL, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.TOTAL_ENTRIES)

        expected = {
            'date': self.TEST_DATA['dates'][0],
            'channel': self.TEST_DATA['channels'][1],
            'country': self.TEST_DATA['countries'][1],
            'os': self.TEST_DATA['os'][1],
            'impressions': self.TEST_DATA['impressions'][1],
            'clicks': self.TEST_DATA['clicks'][1],
            'installs': self.TEST_DATA['installs'][0],
            'spend': self.TEST_DATA['spend'][0],
            'revenue': self.TEST_DATA['revenue'][0],
            'cpi': self.TEST_DATA['spend'][0]/self.TEST_DATA['installs'][0],
        }
        self.assertDictEqual(response.data[0], expected)                                     