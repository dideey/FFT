from rest_framework import serializers
from .models import MonetaryDonation, ClothingDonation, FoodDonation,   Location

class ClothingDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingDonation
        fields = '__all__'

class MonetaryDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonetaryDonation
        fields = '__all__'

class FoodDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDonation
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
