from django.urls import path
from .views import fetch_listing, search_listing

urlpatterns = [
    path('fetch-listings/', fetch_listing, name='fetch_listing'),
    path('search-listings/', search_listing, name='search_listing'),

]
