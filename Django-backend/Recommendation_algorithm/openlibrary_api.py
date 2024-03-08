# openlibrary_api.py (in your Django app)

import requests

class OpenLibraryAPI:
    base_url = 'https://openlibrary.org'

    @classmethod
    def search_books(cls, query):
        url = f'{cls.base_url}/search.json?q={query}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    # Add other API methods as needed (e.g., search_authors, get_book_details, etc.)
