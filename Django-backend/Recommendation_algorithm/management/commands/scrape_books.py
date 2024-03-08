# Recommendation_algorithm/management/commands/scrape_books.py
from django.core.management.base import BaseCommand
from Recommendation_algorithm.utils import scrape_book_metadata
from Recommendation_algorithm.models import Book

class Command(BaseCommand):
    help = 'Scrape book metadata and store it in the database'

    def handle(self, *args, **kwargs):
        # Example book URLs to scrape metadata from
        book_urls = ['https://www.example.com/book1', 'https://www.example.com/book2']
        
        for url in book_urls:
            metadata = scrape_book_metadata(url)
            if metadata:
                Book.objects.create(
                    title=metadata['title'],
                    author=metadata['author'],
                    genre=metadata['genre'],
                    publication_year=metadata['publication_year']
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully scraped and stored metadata for {metadata["title"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'Failed to scrape metadata for {url}'))
