from django.contrib import admin
from .models import MonetaryDonation, ClothingDonation, FoodDonation, Location

# Register your models here.
admin.site.register(MonetaryDonation)
admin.site.register(ClothingDonation)
admin.site.register(FoodDonation)
admin.site.register(Location)