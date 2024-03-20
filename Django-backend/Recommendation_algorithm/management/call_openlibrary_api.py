# Recommendation_algorithm/management/call_openliberary_api.py
import requests

def call_openlibrary_api(identifier, search=False):
    base_url = 'https://openlibrary.org'

    if search:
        url = f'{base_url}/search.json?q={identifier}'
    else:  # Assume ISBN
        url = f'{base_url}/isbn/{identifier}.json'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None  # Indicate failure
