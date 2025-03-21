from django.shortcuts import render
from .models import ReporteIncidente, UserPermission
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseNotFound
from django.core.files.base import File
from django.http import FileResponse



@login_required(login_url = 'login')
def incident_list(request):
    incidents = ReporteIncidente.objects.all()
    user_permission = UserPermission.objects.get(user = request.user)
    context = {
        'incidents': incidents, 
        'user_permission': user_permission,
        }
    return render(request, 'incident_list.html', context)


@login_required(login_url = 'login')
def view_pdf(request, pk):
    try:
        incident = ReporteIncidente.objects.get(pk = pk)
    except ReporteIncidente.DoesNotExist:
        raise Http404("El reporte de incidente no existe")
    if request.method == 'GET':
        response = FileResponse(open(incident.pdf_file.path, 'rb'))
        # response['Content-Disposition'] = f'inline; filename="{incident.pdf_file.name}"'
        return response
    else:
        return HttpResponseNotFound("El reporte de incidente no existe")
