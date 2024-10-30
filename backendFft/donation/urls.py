from .views import ClothingDonationViewSet, MonetaryDonationViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(r'donation', ClothingDonationViewSet, basename='donation')
routers.register(r'monetary', MonetaryDonationViewSet, basename='monetary')

urlpatterns = [
    path('', include(routers.urls)),
]