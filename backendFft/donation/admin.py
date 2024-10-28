from django.contrib import admin
from .models import Donation, ClothingDonation, FoodDonation, Location

# Register your models here.
admin.site.register(Donation)
admin.site.register(ClothingDonation)
admin.site.register(FoodDonation)
admin.site.register(Location)