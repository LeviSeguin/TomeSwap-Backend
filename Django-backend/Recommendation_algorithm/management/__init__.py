# Recommendation_algorithm/management/__init__.py
from django.core.management.base import BaseCommand
from Recommendation_algorithm.management.commands.scrape_books import Command as ScrapeBooksCommand
from Recommendation_algorithm.management.commands.normalize_years import Command as NormalizeYearsCommand

__all__ = [
    'BaseCommand',
    'ScrapeBooksCommand',
    'NormalizeYearsCommand',
]
