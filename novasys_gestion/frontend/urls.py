from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accueil/', views.DashboardView.as_view(), name='dashboard')
]
