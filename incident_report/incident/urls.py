from django.contrib import admin
from django.urls import path
from incident import views



urlpatterns = [
    path('', views.incident_list, name="incident_list"),
    path('create/', views.incident_create, name="incident_create"),
    path('profile/', views.profile, name="profile"),
]