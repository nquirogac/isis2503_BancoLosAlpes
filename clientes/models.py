from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Cliente(Usuario):
    income = models.FloatField(null = False, blank = False)
    debt = models.FloatField(null = False, blank = False)
    economicActivity = models.CharField(max_length = 150)
    company = models.CharField(max_length = 100)
    profession = models.CharField(max_length = 150)
    
    
def __str__(self):
    return f"{self.document} {self.name} {self.email} {self.income} {self.debt}"
