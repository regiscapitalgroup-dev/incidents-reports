from django.db import models

# Create your models here.
CATEGORIAS = [
    ('Accidente', 'Accidente'),
    ('Incendio', 'Incendio'),
    ('Robo', 'Robo'),
    ('Otros', 'Otros'),
]



class Incident(models.Model):
    incident_id = models.AutoField(primary_key=True)
    incident_type = models.CharField(max_length=255)
    incident_category = models.CharField(max_length=15, choices=CATEGORIAS, default='Accidente')
    incident_description = models.TextField()
    incident_date = models.DateTimeField(auto_now_add=True)
    incident_location = models.CharField(max_length=255)
    incident_image = models.FileField(upload_to='incident_files/', null=True, blank=True)


    def __str__(self):
        return self.incident_type + " " + self.incident_location
