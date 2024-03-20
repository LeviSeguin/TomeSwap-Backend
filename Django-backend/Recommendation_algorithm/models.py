# recommendation_algorithm/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BookInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    interaction_type = models.CharField(max_length=20)  # e.g., 'view', 'add', 'rating'

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    # Add other metadata attributes as needed

# Create your models here.
