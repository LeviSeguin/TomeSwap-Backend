# recommendations/views.py

from django.http import JsonResponse
from .models import Book
from .utils import get_recommendations

def book_recommendations(request, book_id):
    book = Book.objects.get(id=book_id)
    recommendations = get_recommendations(book)
    # Format recommendations as needed
    return JsonResponse({'recommendations': recommendations})
