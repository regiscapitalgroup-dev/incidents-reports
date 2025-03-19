from django.contrib import admin
from .models import Incident, IncidentType, IncidentCategory, IncidentLocation, Client
# Register your models here.


admin.site.register(Incident)
admin.site.register(IncidentType)
admin.site.register(IncidentCategory)
admin.site.register(IncidentLocation)
admin.site.register(Client)
