from django.db import models

# Create your models here.
class Donation(models.Model):
    amount = models.FloatField()
    donor = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

class ClothingDonation(models.Model):
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    donor = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    drop_off_location = models.CharField(max_length=100)
    donation_status = models.BooleanField(default=False)

class FoodDonation(models.Model):
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    donor = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    drop_off_location = models.CharField(max_length=100)
    donation_status = models.BooleanField(default=False)

class DonationSummary(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()
    total_monetary_donation = models.FloatField()
    total_clothing_donation = models.IntegerField()
    total_food_donation = models.IntegerField()

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)