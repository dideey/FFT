from django.shortcuts import render
from .models import ClothingDonation
from .serializers import ClothingDonationSerializer
from rest_framework import viewsets
# Create your views here.

class ClothingDonationViewSet(viewsets.ModelViewSet):
    queryset = ClothingDonation.objects.all()
    serializer_class = ClothingDonationSerializer