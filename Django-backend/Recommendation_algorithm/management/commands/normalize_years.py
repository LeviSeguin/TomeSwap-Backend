# Recommendation_algorithm/management/commands/normalize_years.py
from django.core.management.base import BaseCommand
from Recommendation_algorithm.utils import normalize_data
from Recommendation_algorithm.models import Book

class Command(BaseCommand):
    help = 'Normalize publication years of books in the database'

    def handle(self, *args, **kwargs):
        publication_years = Book.objects.values_list('publication_year', flat=True)
        if publication_years:
            normalized_years = normalize_data([[year] for year in publication_years])
            for i, book in enumerate(Book.objects.all()):
                book.publication_year = normalized_years[i][0]
                book.save()
            self.stdout.write(self.style.SUCCESS('Publication years normalized successfully'))
        else:
            self.stdout.write(self.style.WARNING('No publication years found in the database'))
