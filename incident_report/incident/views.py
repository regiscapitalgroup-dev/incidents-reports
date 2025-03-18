from django.shortcuts import render
from .models import Incident
from .forms import IncidentForm
from django.shortcuts import redirect
# Create your views here.


def incident_list(request):
    incidents = Incident.objects.all()
    return render(request, 'incident_list.html', {'incidents': incidents})



def incident_create(request):
    form = IncidentForm()
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('incident_list')
    return render(request, 'incident_create.html', {'form': form})


def profile(request):
    return render(request, 'pages/profile/overview.html')


