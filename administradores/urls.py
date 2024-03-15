from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import postAdministrador, administradoresList

urlpatterns = [
    path('administradores/', administradoresList),
    path('createAdministrador', csrf_exempt(postAdministrador), name = 'createAdministrador' )
]