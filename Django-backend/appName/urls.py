from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, get_user_email

router = DefaultRouter()
router.register('items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_user_email/', get_user_email, name='get_user_email'),
]