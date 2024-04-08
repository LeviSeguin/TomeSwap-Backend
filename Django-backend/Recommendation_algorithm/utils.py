# Recommendation_algorithm/utils.py
import requests
from bs4 import BeautifulSoup
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def scrape_book_metadata(book_url):
    try:
        response = requests.get(book_url)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch book metadata: {e}")
        return None

    if response.status_code != 200:
        print(f"Failed to fetch book metadata: HTTP status code {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    title = None
    title_element = soup.find('h1', {'id': 'bookTitle'})
    if title_element is not None:
        title = title_element.text.strip()

    author = None
    author_element = soup.find('span', {'itemprop': 'author'})
    if author_element is not None:
        author = author_element.text.strip()

    genre = None
    genre_element = soup.find('a', {'class': 'actionLinkLite bookPageGenreLink'})
    if genre_element is not None:
        genre = genre_element.text.strip()

    publication_year = None
    publication_year_element = soup.find('div', {'class': 'uitext darkGreyText'})   
    if publication_year_element is not None:
        publication_year = publication_year_element.text.strip().split()[-1]

    return {
        'title': title,
        'author': author,
        'genre': genre,
        'publication_year': publication_year
    }
    
def normalize_data(data):
    if not isinstance(data, np.ndarray):
        raise ValueError("Input data must be a NumPy array")

    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data.reshape(-1, 1))

    if np.any(np.isnan(normalized_data)) or np.any(np.isinf(normalized_data)):
        raise ValueError("Normalized data contains NaN or Inf values")

    return normalized_data