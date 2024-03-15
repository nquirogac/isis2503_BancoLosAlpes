from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import create_solicitud, solicitudesList

urlpatterns = [
    path('solicitudes/', solicitudesList),
    path('createSolicitud', csrf_exempt(create_solicitud), name = 'createSolicitud'),
]
