from django.test import TransactionTestCase
from unittest.mock import patch, Mock

from taller_test_unitarios.apps.offers.price import calculate_price, get_random_number

def request_get_returns_20():
    requestMock = Mock()

    jsonResponseMock = Mock()
    jsonResponseMock.json.return_value = [{"random": 20}]
    requestMock.get.return_value = jsonResponseMock

    return requestMock

class OfferPriceTestCase(TransactionTestCase):
    @patch('taller_test_unitarios.apps.offers.price.requests', new=request_get_returns_20())
    def test_get_random_number_send_a_request_to_api_and_returns_a_number(self):
        random_number = get_random_number()

        self.assertEqual(random_number, 20)

    @patch('taller_test_unitarios.apps.offers.price.requests')
    def test_calculate_price_return_price_multiplied_by_random_numer(self,  requestMock):
        jsonResponseMock = Mock()
        jsonResponseMock.json.return_value = [{"random": 20}]
        requestMock.get.return_value = jsonResponseMock

        initial_price = 100

        calculated_price = calculate_price(initial_price)

        self.assertEqual(calculated_price, 2000)