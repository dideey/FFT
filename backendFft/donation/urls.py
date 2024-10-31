from .views import ClothingDonationViewSet, MonetaryDonationViewSet, FoodDonationViewSet, LocationViewSet, LocationListView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(r'donation', ClothingDonationViewSet, basename='donation')
routers.register(r'monetary', MonetaryDonationViewSet, basename='monetary')
routers.register(r'food', FoodDonationViewSet, basename='food')
routers.register(r'location', LocationViewSet, basename='location')

urlpatterns = [
    path('', include(routers.urls)),
    path('location/list/', LocationListView.as_view(), name='location-list')
]