from .views import ClothingDonationViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(r'donation', ClothingDonationViewSet, basename='donation')

urlpatterns = [
    path('clothes/', include(routers.urls)),
]