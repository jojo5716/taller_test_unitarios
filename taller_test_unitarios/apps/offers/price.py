import requests

RANDOM_NUMBER_URL = 'https://csrng.net/csrng/csrng.php?min=1&max=100'

def get_random_number():
    response = requests.get(RANDOM_NUMBER_URL)

    return response.json()[0]['random']

def calculate_price(initial_price):
    random_number = get_random_number()

    return initial_price * random_number
