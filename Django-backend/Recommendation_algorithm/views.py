# recommendations/views.py
from django.http import JsonResponse
from .utils import get_recommendations
from .models import Book

def book_recommendations(request, book_id):
    # Assuming book_id is used to identify the book for which recommendations are needed
    book = Book.objects.get(id=book_id)
    recommendations = get_recommendations(book)
    return JsonResponse({'recommendations': recommendations})
