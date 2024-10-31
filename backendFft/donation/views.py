from .models import ClothingDonation, MonetaryDonation, FoodDonation, Location
from .serializers import ClothingDonationSerializer, MonetaryDonationSerializer, FoodDonationSerializer, LocationSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, AllowAny

# Create your views here.

class ClothingDonationViewSet(viewsets.ModelViewSet):
    queryset = ClothingDonation.objects.all()
    serializer_class = ClothingDonationSerializer

class MonetaryDonationViewSet(viewsets.ModelViewSet):
    queryset = MonetaryDonation.objects.all()
    serializer_class = MonetaryDonationSerializer

class FoodDonationViewSet(viewsets.ModelViewSet):
    queryset = FoodDonation.objects.all()
    serializer_class = FoodDonationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAdminUser]

class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [AllowAny]
