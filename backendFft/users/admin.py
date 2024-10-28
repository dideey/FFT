from django.contrib import admin
from . import models
from .models import CustomUser
# Register your models here.
admin.site.register(models.CustomUser)

