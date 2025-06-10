# config/admin.py
from django.contrib import admin

admin.site.site_header = "NOVASYS - Administration des interventions"
admin.site.site_title = "Tableau de bord NOVASYS"
admin.site.index_title = "Gestion des interventions"

# Tri par nom d'applications
admin.AdminSite.index_template = 'admin/custom_index.html'