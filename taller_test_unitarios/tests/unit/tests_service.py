from django.test import TransactionTestCase
from unittest.mock import patch, Mock

from taller_test_unitarios.apps.offers.services import list, create
from ..helpers.offers import create_multiple_offers

class OfferTestCase(TransactionTestCase):
    def setUp(self) -> None:
        with patch('taller_test_unitarios.apps.offers.services.calculate_price') as priceMocked:
            priceMocked.return_value = 200
            create_multiple_offers()

    def test_offer_list_returns_3_offers(self):
        offers = list()

        self.assertEqual(offers.count(), 3)

    @patch('taller_test_unitarios.apps.offers.services.calculate_price')
    def test_create_offer_add_new_offer(self, mocked_calculate_price):
        mocked_calculate_price.return_value = 300
        create({
            "name": f"Offer 4",
            "price": 100
        })

        offers = list()
        last_offer = offers.last()

        self.assertEqual(offers.count(), 4)
        self.assertEqual(last_offer.price, 300)
        
        mocked_calculate_price.assert_called_once_with(100)
