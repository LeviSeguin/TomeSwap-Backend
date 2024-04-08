# Recommendation_algorithm/urls.py

from django.urls import path
from .views import view_book, add_to_library, rate_book, search_books, book_details  # Import book_details here

urlpatterns = [
    path('view-book/', view_book.as_view(), name='view_book'),
    path('add-to-library/', add_to_library.as_view(), name='add_to_library'),
    path('rate-book/', rate_book.as_view(), name='rate_book'),
    path('search-books/', search_books, name='search_books'),
    path('book_details/<str:book_id>/', book_details, name='book_details'),  # Use book_details here
]
