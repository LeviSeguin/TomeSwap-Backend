# recommendation_algorithm/models.py
from django.db import models
from django.contrib.auth.models import User  # Assuming standard User model

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20, unique=True)  # ISBN is unique
    genre = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    description = models.TextField(default='')  # Allow for longer descriptions

class BookInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-add timestamp
    interaction_type = models.CharField(max_length=20, choices=[
        ('VIEW', 'View'),
        ('ADD', 'Add to Library'),
        ('RATE', 'Rating'),
        # Add other interaction types as needed 
    ])
    rating = models.IntegerField(null=True, blank=True)  # Optional rating, can be null
