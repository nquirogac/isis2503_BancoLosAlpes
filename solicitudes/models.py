from django.db import models

class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.

