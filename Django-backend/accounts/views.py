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
    print(serializer.errors)
    return Response(serializer.errors, status=400)

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

        if user is not None:
            login(request, user)
            response_data = {'message': 'Login successful'}
            if request.user.is_authenticated:
                # Retrieve the logged-in user's username
                username = request.user.username
                # Print the username to the terminal
                print("User is authenticated:", username)
                response_data['user authenticated '] = username
            else:
                print("User is not authenticated")
            if 'session_key' in request.session:
                print("Session key:", request.session.session_key)
            else:
                print("No session key found.")
                
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


#User logout
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})




def check_status(request):
    if 'session_key' in request.session:
        print("Session key:", request.session.session_key)
    else:
        print("No session key found.")
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Retrieve the logged-in user's username
        username = request.user.username
        # Return a JSON response with the username
        return JsonResponse({'username': username})
    else:
        # Return a JSON response indicating the user is not authenticated
        print("not authenticated zzz")
        return JsonResponse({'error': 'User is not authenticated'}, status=401)
