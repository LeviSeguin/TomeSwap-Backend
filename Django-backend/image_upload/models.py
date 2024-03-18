from django.db import models
from django.contrib.auth.models import User

class listing(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)
    username = models.CharField(max_length=255, default="test")
    #username = models.ForeignKey(User, on_delete=models.CASCADE)
    listingid = models.AutoField(primary_key=True)
    thumbnail = models.CharField(max_length=255)
    
class Meta:
        db_table = 'image_upload_listing'  # Specify the desired table name

def __str__(self):
    return self.title