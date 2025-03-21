from django.shortcuts import render, redirect
from .models import ReporteIncidente
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('incident_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form})


@login_required(login_url = 'login')
def incident_list(request):
    incidents = ReporteIncidente.objects.all()
    return render(request, 'incident_list.html', {'incidents': incidents})



#def incident_create(request):
#    form = IncidentForm()
#    if request.method == 'POST':
#        form = IncidentForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('incident_list')
#    return render(request, 'incident_create.html', {'form': form})
