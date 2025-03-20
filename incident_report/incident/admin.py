from django.contrib import admin
from .models import Incident, IncidentType, IncidentCategory, IncidentLocation, Company, Branch, Permission, UserPermition


admin.site.site_header = "Reporte de Incidentes"
admin.site.site_title = "Reporte de Incidentes"
admin.site.index_title = "Bienvenido al sistema de reporte de incidentes"


class IncidentAdmin(admin.ModelAdmin):
    list_display = ('incident_type', 'incident_category', 'incident_location', 'incident_company', 'incident_branch')
    list_filter = ('incident_type', 'incident_category', 'incident_location', 'incident_company', 'incident_branch')
    search_fields = ('incident_type', 'incident_category', 'incident_location', 'incident_company', 'incident_branch')
    list_per_page = 10
    list_max_show_all = 100
    readonly_fields = ('incident_id', 'incident_date')



class PermissionAdmin(admin.ModelAdmin):
    list_display = ('permission_name', 'permission_is_viewer', 'permission_is_supervisor', 'permission_is_admin')
    list_per_page = 10
    list_max_show_all = 100


admin.site.register(Incident, IncidentAdmin)
admin.site.register(IncidentType)
admin.site.register(IncidentCategory)
admin.site.register(IncidentLocation)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(UserPermition)
