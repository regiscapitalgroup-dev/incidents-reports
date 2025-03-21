from django.contrib import admin
from .models import IncidentType, IncidentCategory, IncidentLocation, Company, Branch, Permission, UserPermission, ReporteIncidente, EstatusReporte


admin.site.site_header = "Reporte de Incidentes"
admin.site.site_title = "Reporte de Incidentes"
admin.site.index_title = "Bienvenido al sistema de reporte de incidentes"


class PermissionAdmin(admin.ModelAdmin):
    list_display = ('permission_name', 'permission_elevate', 'permission_reporte_semanal_herramienta', 'permission_reporte_quincenal_biometrico', 'permission_reporte_semanal_drones', 'permission_reporte_semanal_cctv820', 'permission_reporte_mantenimiento_drone', 'permission_boletin_ciberseguridad')
    list_per_page = 10
    list_max_show_all = 100


class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'branch', 'permission')
    list_filter = ('company', 'branch', 'permission')
    list_per_page = 10
    list_max_show_all = 100

admin.site.register(Permission, PermissionAdmin)
admin.site.register(UserPermission, UserPermissionAdmin)


class ReporteIncidenteAdmin(admin.ModelAdmin):
    list_display = ('report_date', 'company', 'branch', 'tipo_reporte', 'categoria_reporte')
    list_filter = ('company', 'branch', 'tipo_reporte', 'categoria_reporte')
    list_per_page = 10
    list_max_show_all = 100


admin.site.register(IncidentType)
admin.site.register(IncidentCategory)
admin.site.register(IncidentLocation)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(ReporteIncidente, ReporteIncidenteAdmin)
admin.site.register(EstatusReporte)