from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import postCliente, clientesList

urlpatterns = [
    path('clientes/', clientesList),
    path('createCliente', csrf_exempt(postCliente), name = 'createCliente' )
]