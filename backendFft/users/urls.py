from rest_framework import viewsets, routers
from django.urls import path, include
from .models import CustomUser
from .views import UserViewSet

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)

urlpatterns = [
path('', include(routers.urls)),

]