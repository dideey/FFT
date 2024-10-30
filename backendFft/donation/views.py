from django.shortcuts import render
from .models import ClothingDonation, MonetaryDonation
from .serializers import ClothingDonationSerializer, MonetaryDonationSerializer
from rest_framework import viewsets
# Create your views here.

class ClothingDonationViewSet(viewsets.ModelViewSet):
    queryset = ClothingDonation.objects.all()
    serializer_class = ClothingDonationSerializer

class MonetaryDonationViewSet(viewsets.ModelViewSet):
    queryset = MonetaryDonation.objects.all()
    serializer_class = MonetaryDonationSerializer
