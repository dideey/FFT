from django.contrib import admin
from .models import VolunteerEvent, VolunteerRegistration
# Register your models here.
admin.site.register(VolunteerEvent)
admin.site.register(VolunteerRegistration)
