# Recommendation_algorithm/urls.py

from django.urls import path
from .views import book_recommendations

urlpatterns = [
    path('recommendations/<int:book_id>/', book_recommendations, name='book_recommendations'),
]
