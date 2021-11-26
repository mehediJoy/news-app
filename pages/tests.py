from django.contrib.auth import get_user_model
from django.http import response
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomePageTests(SimpleTestCase):
    
    def test_home_page_status_code(self):
        response = self.client.get('/')