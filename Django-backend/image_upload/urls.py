from django.urls import path
from .views import upload_image, save_book

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('save-book/', save_book, name='save_book'),    
]
