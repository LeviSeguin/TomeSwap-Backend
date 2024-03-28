# Recommendation_algorithm/management/commands/scrape_books.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from Recommendation_algorithm.models import Book
from django.core.management.base import BaseCommand
from Recommendation_algorithm.management import call_openlibrary_api, call_googlebooks_api
from Recommendation_algorithm.models import Book
from call_openlibrary_api import call_openlibrary_api
from call_googlebooks_api import call_googlebooks_api
from sklearn.feature_extraction.text import TfidfVectorizer

class Command(BaseCommand):
    help = 'Populate book database using Open Library and Google Books APIs, and a fixture file'

    def handle(self, *args, **kwargs):
        # Initialize the dictionary
        self._book_descriptions = {}
        isbn_list = ['9780596520687', '9780345391803', '9781593279509']
        search_queries = ['Python Programming', 'The Lord of the Rings']

        # Create the example books for the fixture
        example_books = [
            {
                'title': 'Example Book 1',
                'author': 'Author 1',
                'isbn': '9780000000011',
                'genre': 'Test Genre',
                'publication_year': '2000',
            },
            {
                'title': 'Example Book 2',
                'author': 'Author 2',
                'isbn': '9780000000022',
                'genre': 'Test Genre',
                'publication_year': '2001',
            },
            {
                'title': 'Example Book 3',
                'author': 'Author 3',
                'isbn': '9780000000033',
                'genre': 'Test Genre',
                'publication_year': '2002',
            },
        ]

        for isbn in isbn_list:
            self._process_book_data_open_library(call_openlibrary_api(isbn))
            self._process_book_data_google_books(call_googlebooks_api(isbn))

        for query in search_queries:
            books_data = call_openlibrary_api(query, search=True)
            if books_data:
                for book in books_data['docs']:
                    self._process_book_data_open_library(book)

    def _process_book_data_open_library(self, book_data):
        if not Book.objects.filter(isbn=book_data.get('isbn')).exists():
            description = book_data.get('description', '')
            goodreads_data = self._scrape_goodreads(book_data['isbn'])
            description += goodreads_data[0]   
            Book.objects.create(
        title=book_data.get('title', ''),
        author=book_data.get('author', ''),
        isbn=book_data.get('isbn', ''),
        genre=book_data.get('genre', ''),
        publication_year=book_data.get('publication_year', ''),
)
            self.stdout.write(self.style.SUCCESS(f'Book added: {book_data["title"]}'))
        else:
            self.stdout.write(self.style.NOTICE(f'Book with ISBN {book_data["isbn"]} already exists')) 

    def _scrape_goodreads(self, book_isbn):
    # ... Use 'requests' or Beautiful Soup to fetch data from Goodreads
    description = ...  # Extract book description
    reviews = ...  # Extract reviews (optional)
    return description, reviews 

    def _scrape_googlebooks(self):
        # Implement scraping from Google Books API
        
    # ... Other imports

    def _process_book_data_google_books(self, book_data):
     description = book_data.get('description', '')
     self._book_descriptions[book_data['isbn']] = description
# Store descriptions for later use

    # Assuming 'description' is available from the APIs or scraping
     description = book_data.get('description', '')
     self._book_descriptions[book_data['isbn']] = description 
    # Store descriptions for later use

# In a different script where you build the content-based component:
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(self._book_descriptions.values()) 

# Function for calculating recommendations based on a book's ISBN:
def get_content_based_recommendations(book_isbn, top_n=5):
  book_index = self._book_descriptions.keys().index(book_isbn)
  similarities = cosine_similarity(tfidf_matrix[book_index], tfidf_matrix).flatten()
  # ... rest of the logic to get top recommendations
