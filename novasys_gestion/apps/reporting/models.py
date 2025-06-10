# reporting/models.py
from django.db import models
from apps.interventions.models import Intervention


class RapportIntervention(models.Model):
    intervention = models.OneToOneField(
        Intervention,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='rapport'
    )
    contenu = models.TextField()
    notes_techniques = models.TextField(blank=True)
    feedback_client = models.TextField(blank=True)
    signature_technicien = models.BooleanField(default=False)
    signature_client = models.BooleanField(default=False)
    date_signature_technicien = models.DateTimeField(null=True, blank=True)
    date_signature_client = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Rapport d'intervention"
        verbose_name_plural = "Rapports d'intervention"

    def __str__(self):
        return f"Rapport {self.intervention.code_intervention}"