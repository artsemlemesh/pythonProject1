from django.test import TestCase, Client
from django.urls import reverse
from . import views
import json


class TestViews(TestCase):
    def test_list_perevals(self):
        client = Client()

        response = client.get(reverse('submitData/'))

        self.assertEqual(response.status_code, 200)

