from django.db import models

class Solicitud(models.Model):
    creationDate = models.DateTimeField(auto_now_add = True)
    closeDate = models.DateField(null = True)
    status = models.CharField(max_length = 50)

def __str__(self):
    return '%s %s %s' % (self.creationDate, self.status, self.closeDate)
