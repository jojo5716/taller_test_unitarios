from django.test import TransactionTestCase
from django.test import RequestFactory
from unittest.mock import patch
from collections import OrderedDict

from ..helpers.offers import create_multiple_offers
from taller_test_unitarios.apps.offers.views import OfferView

class OfferCrudTest(TransactionTestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()

        with patch('taller_test_unitarios.apps.offers.services.calculate_price') as priceMocked:
            priceMocked.return_value = 200
            create_multiple_offers()
    
    def test_list_endpoint_returns_all_offers(self):
        request = self.factory.get('http://localhost:8000/offers/')

        response = OfferView.as_view({'get': 'list'})(request)
        response_body = response.data
        expected_offers = [
            OrderedDict([('name', 'Offer 1'), ('price', 200.0)]), 
            OrderedDict([('name', 'Offer 2'), ('price', 200.0)]), 
            OrderedDict([('name', 'Offer 3'), ('price', 200.0)])
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_body), 3)
        self.assertEqual(expected_offers, response_body)
    