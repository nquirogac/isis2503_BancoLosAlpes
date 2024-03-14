from django.db import models

class Solicitud(models.Model):
    userId = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s' % (self.userId, self.operation, self.created_at)

# Create your models here.

