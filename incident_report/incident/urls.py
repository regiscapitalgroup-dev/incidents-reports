from django.contrib import admin
from django.urls import path
from incident import views



urlpatterns = [
    path('', views.incident_list, name = 'incident_list'),
    path('view_pdf/<int:pk>/', views.view_pdf, name = 'view_pdf'),
]