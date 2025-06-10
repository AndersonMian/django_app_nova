# clients/models.py
from django.db import models


class Client(models.Model):
    TYPE_CLIENT_CHOICES = [
        ('entreprise', 'Entreprise'),
        ('particulier', 'Particulier'),
    ]

    nom = models.CharField(max_length=200)
    type_client = models.CharField(max_length=20, choices=TYPE_CLIENT_CHOICES)
    adresse = models.TextField()
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    reference_client = models.CharField(max_length=50, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['nom']

    def __str__(self):
        return f"{self.nom} ({self.reference_client})"