from rest_framework import serializers
from .models import Intervention
from .models import TechnicianLocation
from django.contrib.auth.models import User
from .models import Client

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        
class TechnicianLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicianLocation
        fields = ['technician_id', 'latitude', 'longitude', 'updated_at']

class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = '__all__'

    def validate(self, data):
        # Si on essaie d'ajouter une signature mais que le statut n'est pas "done"
        if data.get("client_signature") and data.get("status") != "done":
            raise serializers.ValidationError("La signature ne peut être ajoutée que lorsque l'intervention est terminée.")
        return data
    
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'