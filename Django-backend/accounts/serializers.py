
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

# For sanitization of user account creation input
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')  # Add any other fields you want to include
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

    #hashing password
    def create(self, validated_data):
        # Hash the password before saving the user
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
