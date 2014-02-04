from django.test import TestCase
from django.test import Client
# Create your tests here.

class BlogViewsTestCase(TestCase):

    def setup(self):
        self.client = Client()

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    
