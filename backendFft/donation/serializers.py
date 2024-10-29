from rest_framework import serializers
from .models import Donation, ClothingDonation

class ClothingDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingDonation
        fields = '__all__'