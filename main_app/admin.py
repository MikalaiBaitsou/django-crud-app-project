from django.contrib import admin

# Register your models here.
from .models import Property, Appointment

# this creates a CRUD for a our Property model in the django admin app
admin.site.register(Property)
admin.site.register(Appointment)