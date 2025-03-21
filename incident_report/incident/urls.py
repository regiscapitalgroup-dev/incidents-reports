from django.contrib import admin
from django.urls import path
from incident import views



urlpatterns = [
    path('login/', views.user_login, name = 'login'),
    path('', views.incident_list, name = 'incident_list'),

]