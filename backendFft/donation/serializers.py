from rest_framework import serializers
from .models import MonetaryDonation, ClothingDonation

class ClothingDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingDonation
        fields = '__all__'

class MonetaryDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonetaryDonation
        fields = '__all__'

