from django.db import models
from usuarios.models import Usuario

class Administrador(Usuario):
    login = models.CharField(max_length = 150)
    password = models.CharField(max_length = 170)
    
def __str__(self):
    return '%s %s %s %s' (str(self.document), self.name, self.email, self.login, self.password)

# Create your models here.
