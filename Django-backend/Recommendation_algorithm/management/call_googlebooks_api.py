# Recommendation_algorithm/management/call_googlebooks_api.py
import requests

def call_googlebooks_api(identifier, search=False):
    base_url = 'https://www.googleapis.com/books/v1/volumes'
    api_key = 'AIzaSyDY5aN6CrUjrjF3V5yoOYZf816t39DWTtI'  # Replace this placeholder

    if search:
        url = f'{base_url}?q={identifier}&key={api_key}'
    else:  # Assume ISBN
        url = f'{base_url}?q=isbn:{identifier}&key={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None  # Indicate failure
