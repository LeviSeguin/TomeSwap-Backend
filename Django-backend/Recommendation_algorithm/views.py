from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookInteraction
from django.http import JsonResponse
import torch
import syft as sy
import pytesseract
from PIL import Image
from sklearn.neighbors import NearestNeighbors
import numpy as np
from .openlibrary_api import OpenLibraryAPI

def search_books(request):
    query = request.GET.get('q', '')
    if query:
        books_data = OpenLibraryAPI.search_books(query)
        return JsonResponse(books_data)
    else:
        return JsonResponse({'error': 'No query parameter provided'}, status=400)


# Sample user-item interaction data (user ratings for books)
user_item_matrix = np.array([[4, 0, 5, 0, 1],
                              [0, 2, 0, 3, 4],
                              [5, 1, 0, 2, 0],
                              [0, 3, 4, 0, 5]])

# Train collaborative filtering model
def train_collaborative_filtering_model():
    model = NearestNeighbors(n_neighbors=2, algorithm='brute', metric='cosine')
    model.fit(user_item_matrix)
    return model

# Generate recommendations for given users
def _generate_recommendations_from_model(user_ids):
    user_indexes = [int(user_id) - 1 for user_id in user_ids]  # Convert user IDs to 0-based indexes
    user_ratings_list = [user_item_matrix[user_index] for user_index in user_indexes]
    user_ratings_array = np.array(user_ratings_list)
    _, neighbor_indices = model.kneighbors(user_ratings_array)
    neighbor_indices_list = [indices[0] for indices in neighbor_indices]
    recommendations_list = [user_item_matrix[neighbor_indices].mean(axis=0) for neighbor_indices in neighbor_indices_list]
    return recommendations_list

# Deploy collaborative filtering model as API endpoint
model = train_collaborative_filtering_model()

@api_view(['POST'])
def view_book(request):
    user = request.user
    book_id = request.data.get('book_id')
    if book_id:
        interaction = BookInteraction.objects.create(user=user, book_id=book_id, interaction_type='view')
        return Response({'message': 'Book viewed successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Missing book_id'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_to_library(request):
    user = request.user
    book_id = request.data.get('book_id')
    if book_id:
        interaction = BookInteraction.objects.create(user=user, book_id=book_id, interaction_type='add')
        return Response({'message': 'Book added to library successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Missing book_id'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def rate_book(request):
    user = request.user
    book_id = request.data.get('book_id')
    rating = request.data.get('rating')
    if book_id and rating:
        interaction = BookInteraction.objects.create(user=user, book_id=book_id, interaction_type='rating', rating=rating)
        return Response({'message': 'Book rated successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Missing book_id or rating'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def generate_recommendations(request):
    user_ids = request.data.get('user_ids')
    if user_ids:
        recommendations = _generate_recommendations_from_model(user_ids)
        return JsonResponse({'recommendations': [rec.tolist() for rec in recommendations]})
    else:
        return Response({'error': 'Missing user_ids'}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def extract_text_from_image(request):
    # Sample view function for extracting text from an image using Tesseract OCR

    # Get image file from request
    image_file = request.FILES.get('image')

    # Open image using PIL (Python Imaging Library)
    image = Image.open(image_file)
    