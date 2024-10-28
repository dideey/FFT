from django.db import models

# Create your models here.
class VolunteerEvent(models.Model):
    event_name = models.CharField(max_length=100)
    location = models.ForeignKey('donation.Location', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    description = models.TextField()
    volunteers = models.ManyToManyField('users.User')

    def __str__(self):
        return self.namr

class VolunteerRegistration(models.Model):
    event = models.ForeignKey('volunteer.VolunteerEvent', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)
    guest_name = models.CharField(max_length=100, blank=True, null=True)
    guest_email = models.EmailField(max_length=100, blank=True, null=True)
    guest_phone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.volunteer.name
    
    def is_guest(self):
        return self.user is None   


class EventSummary(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()
    total_volunteers = models.IntegerField()
    total_guests = models.IntegerField()
    total_events = models.IntegerField()

    def __str__(self):
        return f'Event Summary {self.month}/{self.year}'

  