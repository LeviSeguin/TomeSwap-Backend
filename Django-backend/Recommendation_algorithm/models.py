# models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # Add more fields as needed

class Recommendation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    recommended_book = models.ForeignKey(Book, related_name='recommended_books', on_delete=models.CASCADE)
    score = models.FloatField()
