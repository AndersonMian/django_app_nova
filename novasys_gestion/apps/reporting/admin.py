# reporting/admin.py
from django.contrib import admin
from .models import RapportIntervention

@admin.register(RapportIntervention)
class RapportInterventionAdmin(admin.ModelAdmin):
    list_display = ('intervention', 'signature_status', 'date_signature_technicien')
    readonly_fields = ('intervention',)
    fields = ('intervention', 'contenu', 'notes_techniques', 'feedback_client', 
             ('signature_technicien', 'date_signature_technicien'),
             ('signature_client', 'date_signature_client'))

    def signature_status(self, obj):
        return obj.get_signature_status()
    signature_status.short_description = "État des signatures"