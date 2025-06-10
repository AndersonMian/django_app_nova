# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('interventions/', views.InterventionList.as_view(), name='intervention-list'),
    path('clients/', views.ClientList.as_view(), name='client-list'),
]