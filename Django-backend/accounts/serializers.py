
from rest_framework import serializers
from .models import CustomUser

# For sanitization of user account creation input
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')  # Add any other fields you want to include
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only
