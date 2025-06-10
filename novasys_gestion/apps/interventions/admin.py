# interventions/admin.py
from django.contrib import admin
from .models import Intervention, InterventionHistory


class InterventionHistoryInline(admin.StackedInline):
    model = InterventionHistory
    extra = 0
    readonly_fields = ('date_modification', 'user', 'modifications')
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    list_display = ('code', 'client', 'technicien', 'statut', 'date_creation', 'date_modification')
    list_editable = ('statut',)
    list_filter = ('statut', 'client', 'technicien')
    search_fields = ('code', 'client__nom')
    raw_id_fields = ('client', 'technicien')
    inlines = [InterventionHistoryInline]
    date_hierarchy = 'date_creation'

    fieldsets = (
        (None, {
            'fields': ('code', 'client', 'technicien')
        }),
        ('Détails intervention', {
            'fields': ('description', 'statut', 'date_creation', 'date_modification')
        }),
    )

    def save_model(self, request, obj, form, change):
        if change:
            original = Intervention.objects.get(pk=obj.pk)
            changes = {
                field: {'from': getattr(original, field), 'to': getattr(obj, field)}
                for field in ['statut', 'description']
                if getattr(original, field) != getattr(obj, field)
            }
            if changes:
                obj.historique.create(
                    user=request.user,
                    modifications=changes
                )
        super().save_model(request, obj, form, change)