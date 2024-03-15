from django.db import models
from usuarios.models import Usuario

class Solicitud(models.Model):
    user = models.ForeignKey(Usuario, on_delete = models.CASCADE, default = None)
    creationDate = models.DateTimeField(auto_now_add = True)
    closeDate = models.DateField(null = True, blank= True, default = None)
    status = models.CharField(max_length = 50)

def __str__(self):
    return '%s %s %s %s' % (str(self.user), self.creationDate, self.status, self.closeDate)
