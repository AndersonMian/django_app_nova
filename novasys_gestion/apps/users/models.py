# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('admin', 'Administrateur'),
        ('technicien', 'Technicien'),
    ]

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='technicien'
    )
    phone = models.CharField(max_length=20, blank=True)
    specialite = models.CharField(max_length=100, blank=True)  # Pour les techniciens
    date_embauche = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        ordering = ['last_name']

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_user_type_display()})"
