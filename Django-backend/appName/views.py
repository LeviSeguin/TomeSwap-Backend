from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from accounts.models import CustomUser

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    
    
def get_user_email(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        try:
            user = CustomUser.objects.get(username=username)
            #return JsonResponse({'email': "test"})
            return JsonResponse({'email': user.email})
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)