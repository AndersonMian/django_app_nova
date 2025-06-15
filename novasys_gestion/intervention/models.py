from django.db import models
from django.conf import settings

class TechnicianLocation(models.Model):
    technician = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.technician.username} @ ({self.latitude}, {self.longitude})"


class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Intervention(models.Model):
    STATUS_CHOICES = [
        ('initial', 'Initialisé'),
        ('in_progress', 'En cours'),
        ('done', 'Terminé'),
    ]

    description = models.TextField()
    date = models.DateTimeField()
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='initial')
    technician = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='interventions')
    client_signature = models.TextField(blank=True, null=True)  # base64 ou texte
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # utile pour la sync offline

    def __str__(self):
        return f"Intervention #{self.id} - {self.status}"
