from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length = 150)
    lastName = models.CharField(max_length = 150)
    document = models.BigIntegerField(null = False, blank = False, primary_key=True)
    age = models.IntegerField(null = False, blank = False)
    email = models.CharField(max_length = 250)
    country = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    
    class Meta:
        abstract = True

def __str__(self):
    return f"{self.document} {self.name} {self.email} {self.age}"


