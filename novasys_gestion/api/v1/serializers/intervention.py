# api/v1/serializers/intervention.py
from django.core import serializers

from novasys_gestion.apps.interventions.models import Intervention


class InterventionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intervention
        fields = ['url', 'code', 'statut', 'client', 'technicien']
        extra_kwargs = {
            'url': {'view_name': 'api:v1:intervention-detail'}
        }