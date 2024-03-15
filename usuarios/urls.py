from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import postUsuario, usurariosList

urlpatterns = [
    path('usuarios/', usurariosList),
    path('createUsuario', csrf_exempt(postUsuario), name = 'createUsuario' )
]
