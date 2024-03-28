# Recommendation_algorithm/management/commands/scrape_openlibrary.py
import requests
from bs4 import BeautifulSoup

def _scrape_openlibrary(identifier):
    url = f"https://openlibrary.org/search/{identifier}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        if 'ISBN' in soup:
            isbn = soup['ISBN'][identifier]  # Extract ISBN
        if 'publishers' in soup:
            publisher = soup['publishers'][0]  # Extract publisher

        title = _extract_title(soup)
        author = _extract_author(soup)

        return {
            'title': title,
            'author': author,
            'isbn': isbn,
            'publisher': publisher,
        }
    else:
        return None

# Helper functions to extract data from HTML
def _extract_title(soup):
    title_element = soup.find('h1', {'class': 'title'})
    return title_element.text.strip() if title_element else None

def _extract_author(soup):
    author_element = soup.find('span', {'class': 'author-name'})
    return author_element.text.strip() if author_element else None