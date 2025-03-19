from django.db import models
from django.contrib.auth.models import User


def upload_image_path(instance, filename):
    return f"incident_images/{instance.incident_client.client_id}/{filename}"

def upload_video_path(instance, filename):
    return f"incident_video/{instance.incident_client.client_id}/{filename}"


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)

    def __str__(self):
        return self.client_name


class IncidentLocation(models.Model):
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.location
    

class IncidentType(models.Model):
    incident_type = models.CharField(max_length=255)

    def __str__(self):
        return self.incident_type
    

class IncidentCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Incident(models.Model):
    incident_id = models.AutoField(primary_key=True)
    incident_client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    incident_type = models.ForeignKey(IncidentType, on_delete=models.CASCADE)
    incident_category = models.ForeignKey(IncidentCategory, on_delete=models.CASCADE)
    incident_description = models.TextField()
    incident_date = models.DateTimeField(auto_now_add=True)
    incident_location = models.ForeignKey(IncidentLocation, on_delete=models.CASCADE)
    incident_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    incident_video = models.FileField(upload_to=upload_video_path, null=True, blank=True)
    incident_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.incident_type) + " " + str(self.incident_location)
