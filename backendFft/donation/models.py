from django.db import models

# Create your models here.
class Donation(models.Model):
    amount = models.FloatField()
    donor = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

class ClothingDonation(models.Model):
    type = models.CharField(max_length=100)
    quantity = models.IntergerField()
    donor = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    drop_off_location = models.CharField(max_length=100)

class FoodDonation(models.Model):
    type = models.CharField(max_length=100)
    quantity = models.IntergerField()
    donor = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    drop_off_location = models.CharField(max_length=100)

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

