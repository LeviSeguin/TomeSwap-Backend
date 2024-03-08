# recommendations/urls.py
from django.urls import path
from .views import view_book, add_to_library, rate_book
from .views import search_books

urlpatterns = [
    path('view-book/', view_book, name='view_book'),
    path('add-to-library/', add_to_library, name='add_to_library'),
    path('rate-book/', rate_book, name='rate_book'),
    path('search-books/', search_books, name='search_books'),
]
