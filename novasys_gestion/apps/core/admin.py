# core/admin.py
from django.contrib import admin
from .models import ClientAdresse, TechnicienAdresse
from ..clients.admin import ClientAdmin
from ..users.admin import CustomUserAdmin


class ClientAdresseInline(admin.StackedInline):
    model = ClientAdresse
    can_delete = False
    verbose_name_plural = 'Adresse du client'

class TechnicienAdresseInline(admin.StackedInline):
    model = TechnicienAdresse
    can_delete = False
    verbose_name_plural = 'Adresse du technicien'

# Ajouter ces inlines dans les admins existants


ClientAdmin.inlines = [ClientAdresseInline]
CustomUserAdmin.inlines = [TechnicienAdresseInline]