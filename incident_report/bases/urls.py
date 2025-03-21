from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
]