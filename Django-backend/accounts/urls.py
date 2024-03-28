# urls.py

from django.urls import path

from .views import register_user #user registration
from .views import login_view, logout_view #user login

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]