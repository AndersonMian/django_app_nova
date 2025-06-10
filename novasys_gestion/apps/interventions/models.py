# apps/interventions/models.py
from django.db import models
from apps.users.models import CustomUser
from apps.clients.models import Client


class Intervention(models.Model):
    STATUS_CHOICES = [
        ('initialiser', 'Initialisé'),
        ('en_cours', 'En Cours'),
        ('termine', 'Terminé')
    ]

    code = models.CharField(max_length=20, unique=True)
    technicien = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='interventions_techniquees')
    administrateur = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='interventions_administrees')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_creation']
        verbose_name = "Intervention"
        verbose_name_plural = "Interventions"

    def __str__(self):
        return f"{self.code} - {self.client.nom}"

class InterventionHistory(models.Model):
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE, related_name='historique')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    date_modification = models.DateTimeField(auto_now_add=True)
    modifications = models.JSONField()

    class Meta:
        verbose_name = "Historique d'intervention"
        ordering = ['-date_modification']