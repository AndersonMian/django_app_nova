from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Intervention
from .serializers import InterventionSerializer
from rest_framework.decorators import action

from .models import Client
from .serializers import ClientSerializer

from rest_framework.generics import RetrieveAPIView
from django.contrib.auth.models import User
from rest_framework.exceptions import NotFound

from rest_framework import status

from django.http import HttpResponse
from .pdf_utils import render_to_pdf
from django.template import loader
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import TechnicianLocation
from .serializers import TechnicianLocationSerializer
from rest_framework.generics import RetrieveUpdateAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()

class InterventionViewSet(viewsets.ModelViewSet):
    queryset = Intervention.objects.all()  # <- Ajout obligatoire pour le router
    serializer_class = InterventionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Intervention.objects.all()
        return Intervention.objects.filter(technician=user)
    
    @action(detail=True, methods=['patch'], url_path='assign', url_name='assign-technician')
    def assign_technician(self, request, pk=None):
        try:
            intervention = self.get_object()
            technician_id = request.data.get("technician_id")

            if not technician_id:
                return Response({"error": "technician_id is required"}, status=400)

            # Vérifier que l'utilisateur appartient bien au groupe "Technicien"
            group = Group.objects.get(name="Techniciens")
            technician = group.user_set.filter(id=technician_id).first()

            if not technician:
                return Response({"error": "L'utilisateur spécifié n'est pas un technicien valide."}, status=400)

            intervention.technician = technician
            intervention.save()

            return Response({"success": f"Intervention assignée à {technician.username}"}, status=200)

        except Intervention.DoesNotExist:
            return Response({"error": "Intervention introuvable"}, status=404)
        except Group.DoesNotExist:
            return Response({"error": "Le groupe Technicien n'existe pas"}, status=500)

class TechnicienListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            group = Group.objects.get(name="Techniciens")
            techniciens = group.user_set.all()
            data = [
                {"id": user.id, "username": user.username, "email": user.email}
                for user in techniciens
            ]
            return Response(data)
        except Group.DoesNotExist:
            return Response([])
        

class TechnicianLocationView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TechnicianLocationSerializer

    def get_object(self):
        # Ne crée pas automatiquement si l'objet n'existe pas
        return TechnicianLocation.objects.filter(technician=self.request.user).first()

    def get(self, request, *args, **kwargs):
        location = self.get_object()
        if not location:
            return Response(
                {"detail": "Aucune localisation enregistrée pour ce technicien."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(location)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        # Crée si inexistant (mais cette fois, avec des données valides)
        location, _ = TechnicianLocation.objects.get_or_create(technician=request.user)

        serializer = self.get_serializer(location, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class TechnicianLocationByIdView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TechnicianLocationSerializer
    lookup_url_kwarg = "technician_id"

    def get_object(self):
        technician_id = self.kwargs.get(self.lookup_url_kwarg)
        try:
            technician = User.objects.get(pk=technician_id)
        except User.DoesNotExist:
            raise NotFound("Technicien inexistant.")

        # Si la position n'existe pas encore, retourne un objet factice avec 0,0
        location, created = TechnicianLocation.objects.get_or_create(
            technician=technician,
            defaults={"latitude": 0.0, "longitude": 0.0}
        )
        return location
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_intervention_pdf(request, pk):
    intervention = get_object_or_404(Intervention, pk=pk)

    if request.user != intervention.technician and not request.user.is_staff:
        return HttpResponse("Non autorisé", status=403)

    pdf = render_to_pdf("intervention_report.html", {"intervention": intervention})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')

        # 👇 Ce bloc contrôle l'affichage inline vs téléchargement
        download = request.GET.get('download')
        if download == '1':
            response['Content-Disposition'] = f'attachment; filename="intervention_{pk}.pdf"'
        else:
            response['Content-Disposition'] = f'inline; filename="intervention_{pk}.pdf"'

        return response

    return HttpResponse("Erreur de génération PDF", status=500)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('-created_at')
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]