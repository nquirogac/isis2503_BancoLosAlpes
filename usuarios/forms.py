from django import forms 
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'name',
            'lastName',
            'documuent',
            'age',
            'email',
            'country',
            'city',
        ]
        
        labels = {
            'name':'name',
            'lastName':'lastName',
            'document': 'document',
            'age': 'age',
            'email': 'email',
            'country': 'country',
            'city': 'city',
        }