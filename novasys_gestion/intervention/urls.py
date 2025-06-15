from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InterventionViewSet
from .views import TechnicienListView
from .views import TechnicianLocationView
from .views import TechnicianLocationByIdView
from .views import generate_intervention_pdf
from .views import ClientViewSet
 
router = DefaultRouter()
router.register(r'intervention', InterventionViewSet)
router.register(r'clients', ClientViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('intervention/', include(router.urls)),
    path('techniciens/', TechnicienListView.as_view(), name="techniciens-list"),
    path('techniciens/position/', TechnicianLocationView.as_view(), name="technicien-position"),
    path('technicien/position/<int:technician_id>/', TechnicianLocationByIdView.as_view(), name='technicien-position-by-id'),
    path('intervention/<int:pk>/pdf/', generate_intervention_pdf, name="generate-intervention-pdf"),

]