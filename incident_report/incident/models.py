from django.db import models
from django.contrib.auth.models import User


def upload_file_path(instance, filename):
    return f"incident_files/{instance.incident_company.company_id}/{instance.incident_branch.branch_id}/{filename}"


class Company(models.Model):
    # Soriana
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name
    

class Branch(models.Model):
    # Sucursal de Soriana
    branch_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=255)

    def __str__(self):
        return self.branch_name
    
    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"


class Permission(models.Model):
    # Catálogo de permisos
    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(max_length=255)
    permission_is_viewer = models.BooleanField(default=False)
    permission_is_supervisor = models.BooleanField(default=False)
    permission_is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.permission_name
    
    class Meta:
        verbose_name = "Permiso"
        verbose_name_plural = "Permisos"


class UserPermition(models.Model):
    # Usuario con permisos
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, verbose_name="Permisos")

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Permiso de usuario"
        verbose_name_plural = "Permisos de usuarios"


class IncidentLocation(models.Model):
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciones"


class IncidentType(models.Model):
    incident_type = models.CharField(max_length=255)

    def __str__(self):
        return self.incident_type
    

    class Meta:
        verbose_name = "Tipo de incidente"
        verbose_name_plural = "Tipos de incidentes"


class IncidentCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = "Categoría de incidente"
        verbose_name_plural = "Categorías de incidentes"


class Incident(models.Model):
    incident_id = models.AutoField(primary_key=True)
    incident_company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    incident_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    incident_type = models.ForeignKey(IncidentType, on_delete=models.CASCADE)
    incident_category = models.ForeignKey(IncidentCategory, on_delete=models.CASCADE)
    incident_description = models.TextField()
    incident_date = models.DateTimeField(auto_now_add=True)
    incident_location = models.ForeignKey(IncidentLocation, on_delete=models.CASCADE)
    incident_file = models.FileField(upload_to=upload_file_path, null=True, blank=True)
    incident_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.incident_type) + " " + str(self.incident_location)

    class Meta:
        verbose_name = "Incidente"
        verbose_name_plural = "Incidentes"
