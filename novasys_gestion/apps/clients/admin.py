# clients/admin.py
from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('reference_client', 'nom', 'type_client', 'email', 'telephone')
    list_filter = ('type_client',)
    search_fields = ('nom', 'reference_client', 'email')
    ordering = ('nom',)