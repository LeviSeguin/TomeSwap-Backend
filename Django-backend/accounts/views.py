import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomUserSerializer

# User account registration
@api_view(['POST'])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User login
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        user = authenticate(request, username=username, password=password)
        print(username)
        print(password)
        print(user)
        if user is not None:
            print(2)
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            print(1)
            return JsonResponse({'error': 'Invalid username or password'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

#User logout
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})
