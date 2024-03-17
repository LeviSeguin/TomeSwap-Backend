from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)
    username = models.CharField(max_length=255, default="test")
    #username = models.ForeignKey(User, on_delete=models.CASCADE)
    listingid = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title