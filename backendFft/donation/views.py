from .models import ClothingDonation, MonetaryDonation, FoodDonation, Location
from .serializers import ClothingDonationSerializer, MonetaryDonationSerializer, FoodDonationSerializer, LocationSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView
from django.db import models
from rest_framework.response import Response
from rest_framework import status
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

class DonationSummaryView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, *args, **kwargs):
        monetary_donations = MonetaryDonation.objects.all()
        clothing_donations = ClothingDonation.objects.all()
        food_donations = FoodDonation.objects.all()

        summary = {
            'total_monetary_donations': monetary_donations.count(),
            'total_clothing_donations': clothing_donations.count(),
            'total_food_donations': food_donations.count(),
            'monetary_donations': monetary_donations.aggregate(total_amount=models.Sum('amount')),
            'clothing_donations': clothing_donations.aggregate(total_quantity=models.Sum('quantity')),
            'food_donations': food_donations.aggregate(total_quantity=models.Sum('quantity')),
        }
        return Response(summary, status=status.HTTP_200_OK)