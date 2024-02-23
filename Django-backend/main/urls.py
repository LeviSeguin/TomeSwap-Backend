from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/test/", views.test_api, name="test_api"),
]