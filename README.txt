Récapitulatif complet et structuré de toutes les routes disponibles de l'API, avec :

✅ Méthode
✅ URL complète (exemple avec /api/)
✅ Description
✅ Paramètres (dans l’URL ou le body)
✅ Accès/utilisateurs concernés


                                │                   🧭 ROUTES API DISPONIBLES                      │

🔹 1. Clients

| Méthode | URL                | Description                      | Paramètres/Body                       | Accès       |
| ------- | ------------------ | -------------------------------- | ------------------------------------- | ----------- |
| GET     | /api/intervention/clients/      | Liste tous les clients           | —                                     | Authentifié |
| POST    | /api/intervention/clients/      | Crée un nouveau client           | nom, email, téléphone, adresse        | Authentifié |
| GET     | /api/intervention/clients/{id}/ | Affiche les infos d’un client    | {id} = identifiant client             | Authentifié |
| PATCH   | /api/intervention/clients/{id}/ | Met à jour les infos d’un client | champs partiels (ex. email, adresse…) | Authentifié |
| DELETE  | /api/intervention/clients/{id}/ | Supprime un client               | —                                     | Authentifié |

🔹 2. Interventions

| Méthode | URL                      | Description                | Paramètres/Body                                         | Accès      |
| ------- | ------------------------ | -------------------------- | ------------------------------------------------------- | ---------- |
| GET     | /api/interventions/      | Liste des interventions    | — (ou ?status=initial)                                  | Admin/Tech |
| POST    | /api/interventions/      | Créer une intervention     | description, date, priority, status, technician, client | Admin      |
| GET     | /api/interventions/{id}/ | Détails d’une intervention | —                                                       | Admin/Tech |
| PATCH   | /api/interventions/{id}/ | Modifier une intervention  | champs partiels (ex. status, description, client…)      | Admin/Tech |
| DELETE  | /api/interventions/{id}/ | Supprimer une intervention | —                                                       | Admin      |

🔸 Actions personnalisées :

| Méthode | URL                                           | Description                  | Paramètres/Body                 | Accès      |
| ------- | --------------------------------------------- | ---------------------------- | ------------------------------- | ---------- |
| PATCH   | /api/interventions/{id}/assign/               | Assigne un technicien        | technician\_id                  | Admin      |
| GET     | /api/interventions/{id}/pdf/                  | Génère un rapport PDF        | —                               | Admin/Tech |
| GET     | /api/interventions/sync/?last\_sync=timestamp | Sync interventions modifiées | last\_sync=2025-06-15T13:00:00Z | Admin/Tech |

🔹 3. Techniciens

| Méthode | URL               | Description                       | Paramètres/Body | Accès |
| ------- | ----------------- | --------------------------------- | --------------- | ----- |
| GET     | /api/techniciens/ | Liste des techniciens (du groupe) | —               | Admin |

🔹 4. Géolocalisation des techniciens

| Méthode | URL                                        | Description                                 | Paramètres/Body     | Accès      |
| ------- | ------------------------------------------ | ------------------------------------------- | ------------------- | ---------- |
| GET     | /api/techniciens/position/                 | Récupère la position du technicien connecté | —                   | Technicien |
| PATCH   | /api/techniciens/position/                 | Met à jour sa position                      | latitude, longitude | Technicien |
| GET     | /api/technicien/position/{technician\_id}/ | Voir la position d’un technicien par ID     | —                   | Admin      |

🔹 5. Notifications (FCM)

| Méthode | URL                  | Description                           | Paramètres/Body | Accès      |
| ------- | -------------------- | ------------------------------------- | --------------- | ---------- |
| POST    | /api/register-token/ | Enregistre le token FCM du technicien | token: string   | Technicien |

🔹 6. Actions du technicien

| Action                        | Méthode | URL                          | Test / Exemple                                       |
| ----------------------------- | ------- | ---------------------------- | ---------------------------------------------------- |
| Voir ses interventions        | GET     | /api/interventions/          | → Automatique avec filtrage dans get\_queryset       |
| Changer le statut             | PATCH   | /api/interventions/3/        | { "status": "en\_cours" }                            |
| Faire signer une intervention | POST    | /api/interventions/3/signer/ | { "client\_signature": "data\:image/png;base64..." } |
| Imprimer le rapport (PDF)     | GET     | /api/interventions/3/pdf/    | → Renvoie un PDF                                     |

🔹 7. Pour le mobile
## API Mobile Documentation

### Authentication
**Endpoint**: `POST /api/intervention/mobile-login/`  
**Body**:
```json
{
  "username": "votre_utilisateur",
  "password": "votre_mdp"
}
Reponse Attendu
{
  "token": "abc123...",
  "user_id": 1,
  "username": "tech1",
  "is_technician": true,
  "is_admin": false
}
**Endpoint**: 'GET /api/intervention/sync-interventions/'
**HEADER**: Authorization: "Token abc123..."(exemple)
Reponse attendu
{
  "last_sync": "2023-06-16T12:30:00Z",
  "interventions": [
    {
      "id": 1,
      "description": "Réparation chaudière",
      "status": "in_progress",
      // ... autres champs
    }
  ]
}
