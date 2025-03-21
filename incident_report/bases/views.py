from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('incident_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})


def logout_user(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'home.html')
