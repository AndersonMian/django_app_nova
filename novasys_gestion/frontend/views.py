from django.http import HttpResponse
from django.shortcuts import render

# frontend/views.py
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Données fictives pour la phase frontend
        context.update({
            'interventions_en_cours': 5,
            'clients_actifs': 12,
            'recent_interventions': [
                {
                    'code': 'INT-2023-001',
                    'client': {'nom': 'Client A'},
                    'statut': 'en_cours',
                    'get_statut_display': 'En Cours'
                },
                # Ajouter d'autres entrées...
            ]
        })
        return context


def home(request):
    return render(request, 'index.html')
"""
def dashboard(request):
    return render(request, 'dashboard.html')"""

""""
class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self):
        return {
            'menu': [
                {'name': 'Interventions', 'icon': 'fa-tasks', 'url': 'interventions:list'},
                {'name': 'Clients', 'icon': 'fa-users', 'url': 'clients:list'},
                {'name': 'Rapports', 'icon': 'fa-file-pdf', 'url': 'reporting:generate'}
            ]
        }
"""