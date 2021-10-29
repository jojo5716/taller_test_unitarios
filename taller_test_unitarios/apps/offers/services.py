from .models import Offer
from .price import calculate_price

def list():
    return Offer.objects.all()

def create(validated_data):
    return Offer.objects.create(
        name=validated_data["name"],
        price=calculate_price(validated_data["price"]),
    )