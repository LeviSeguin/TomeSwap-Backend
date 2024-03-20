# Recommendation_algorithm/management/commands/scrape_books.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from Recommendation_algorithm.models import Book
from django.core.management.base import BaseCommand
from Recommendation_algorithm.management import call_openlibrary_api, call_googlebooks_api
from Recommendation_algorithm.models import Book

class Command(BaseCommand):
    help = 'Populate book database using Open Library and Google Books APIs'

    def handle(self, *args, **kwargs):
        # Get a list of ISBNs or Search terms (You can collect these from user input)
        isbn_list = ['9780596520687', '9780345391803']  # Example ISBNs 
        search_queries = ['Python Programming', 'The Lord of the Rings']

        for isbn in isbn_list:
            self._process_book(call_openlibrary_api(isbn))
            self._process_book(call_googlebooks_api(isbn))

        for query in search_queries:
            books_data = call_openlibrary_api(query, search=True)
            if books_data:
                for book in books_data['docs']:
                    self._process_book(book)

    def _process_book(self, book_data):
        # Check if ISBN already exists to avoid duplicates
        if not Book.objects.filter(isbn=book_data.get('isbn')).exists():
            Book.objects.create(
                title=book_data.get('title',''),
                author=book_data.get('author',''),
                isbn=book_data.get('isbn',''),
                genre=book_data.get('genre',''),
                publication_year=book_data.get('publication_year','')
            )
            self.stdout.write(self.style.SUCCESS(f'Book added: {book_data["title"]}'))
        else:
            self.stdout.write(self.style.NOTICE(f'Book with ISBN {book_data["isbn"]} already exists')) 

    def _scrape_goodreads(self):
        book_title = "The Hitchhiker's Guide to the Galaxy"
        search_url = f"https://www.goodreads.com/search?q={book_title}"

        response = requests.get(search_url) 
        response.raise_for_status()  # Check for HTTP Errors

        soup = BeautifulSoup(response.content, 'html.parser')

    # Find the relevant book result (you'll need to refine selectors to be accurate)
        book_element = soup.select_one('.bookTitle')
        if book_element:
            book_title = book_element.get_text().strip()
            book_url = book_element['href']

        # ... (Visit book_url to scrape more details)


def _scrape_googlebooks(self):
    pass
        # Logic to utilize the Google Books API
