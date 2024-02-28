# recommendation_utils.py
from Recommendation_algorithm.models import Book

def get_recommendations(book):
    similar_books = Book.objects.filter(author=book.author).exclude(id=book.id)[:5]
    return [{'title': similar_book.title, 'author': similar_book.author} for similar_book in similar_books]
