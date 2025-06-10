# core/models.py
from django.db import models


class Adresse(models.Model):
    ligne1 = models.CharField(max_length=255)
    ligne2 = models.CharField(max_length=255, blank=True)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100, default='Côte d\'Ivoire')

    class Meta:
        abstract = True


class ClientAdresse(Adresse):
    client = models.OneToOneField(
        'clients.Client',
        on_delete=models.CASCADE,
        related_name='adresses_client'
    )


class TechnicienAdresse(Adresse):
    technicien = models.OneToOneField(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name='adresses'
    )