from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100, verbose_name="Nombre de la Empresa")

    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"


class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Empresa")
    branch_name = models.CharField(max_length=255, verbose_name="Nombre de la Sucursal")

    def __str__(self):
        return self.branch_name
    
    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"



class UserPermission(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Empresa")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="Sucursal")
    permission_elevate = models.BooleanField(default=False, verbose_name="Usuario con permisos Elevados")
    permission_reporte_incidente = models.BooleanField(default=False, verbose_name="Reporte de Incidentes")

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Permiso de usuario"
        verbose_name_plural = "Permisos de usuarios"


class IncidentLocation(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255, verbose_name="Ubicación")

    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciones"


class IncidentType(models.Model):
    id = models.AutoField(primary_key=True)
    incident_type = models.CharField(max_length=255, verbose_name="Tipo de incidente")

    def __str__(self):
        return self.incident_type
    

    class Meta:
        verbose_name = "Tipo de incidente"
        verbose_name_plural = "Tipos de incidentes"


class IncidentCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255, verbose_name="Categoría de incidente")

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = "Categoría de incidente"
        verbose_name_plural = "Categorías de incidentes"


class EstatusReporte(models.Model):
    id = models.AutoField(primary_key=True)
    estatus = models.CharField(max_length=255, verbose_name="Estatus")

    def __str__(self):
        return self.estatus
    
    class Meta:
        verbose_name = "Estatus de reporte"
        verbose_name_plural = "Estatus de reportes"


class ReporteIncidente(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Empresa")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="Sucursal")
    description = models.TextField(verbose_name="Descripción")
    report_date = models.DateField(default=timezone.now, verbose_name="Fecha de reporte")
    tipo_reporte = models.ForeignKey(IncidentType, on_delete=models.CASCADE, verbose_name="Tipo de reporte")
    categoria_reporte = models.ForeignKey(IncidentCategory, on_delete=models.CASCADE, verbose_name="Categoría de reporte")
    estatus_reporte = models.ForeignKey(EstatusReporte, on_delete=models.CASCADE, verbose_name="Estatus de reporte", null=True, blank=True)

    pdf_file = models.FileField(upload_to='reporte_incidente/', verbose_name="Archivo PDF")

    def __str__(self):
        return "Reporte de incidente: {} / {} / {}".format(self.tipo_reporte, self.categoria_reporte, self.report_date)
    
    class Meta:
        verbose_name = "Reporte de incidente"
        verbose_name_plural = "Reportes de incidentes"