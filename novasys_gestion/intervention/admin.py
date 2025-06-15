from django.contrib import admin
from .models import Intervention
from django.contrib.auth.models import Group

class InterventionAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'technician', 'status']
    list_filter = ['status', 'technician']
    search_fields = ['description', 'technician__username']

admin.site.register(Intervention, InterventionAdmin)
# admin.site.register(Group)