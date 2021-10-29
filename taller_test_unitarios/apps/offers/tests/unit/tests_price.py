from django.test import TransactionTestCase, TestCase
from taller_test_unitarios.apps.offers.price import get_random_number

class OfferPriceTestCase(TestCase):
    def setUp(self) -> None:
        print('OfferPriceTestCase \n\n\n\n\n')

    def test_get_random_number_send_a_request_to_api_and_returns_a_number(self):
        random_number = get_random_number()

        self.assertEqual(random_number, 20)