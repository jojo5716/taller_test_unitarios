from taller_test_unitarios.apps.offers.services import create


def create_multiple_offers():
    def _offer_data(index) -> dict:
        return {
            "name": f"Offer {index}",
            "price": 100
        }

    for number in range(1, 4):
        create(_offer_data(number))
