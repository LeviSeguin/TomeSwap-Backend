from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    
    
def get_user_email(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Retrieve the email of the authenticated user
        user_email = request.user.email
        # Return the email as JSON response
        return JsonResponse({'email': user_email})
    else:
        # Return error message if the user is not authenticated
        return JsonResponse({'error': 'User is not authenticated'}, status=401)