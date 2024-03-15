from django import forms
from .models import Administrador

class AdministradorForm(forms.ModelForm):
    
    class Meta:
        model = Administrador
        fields = [
            'name',
            'lastName',
            'document',
            'age',
            'email',
            'country',
            'city',
            'login',
            'password',
        ]
        
        labels = {
            'name':'name',
            'lastName':'lastName',
            'document': 'document',
            'age': 'age',
            'email': 'email',
            'country': 'country',
            'city': 'city',
            'login': 'login',
            'password': 'password',
        }
        
        widgets = {
            'password': forms.PasswordInput(),
        }