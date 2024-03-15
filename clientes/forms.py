from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = [
            'name',
            'lastName',
            'document',
            'age',
            'email',
            'country',
            'city',
            'income',
            'debt',
            'economicActivity',
            'company',
            'profession',
        ]
        
        labels = {
            'name':'name',
            'lastName':'lastName',
            'document': 'document',
            'age': 'age',
            'email': 'email',
            'country': 'country',
            'city': 'city',
            'income': 'income',
            'debt': 'debt',
            'economicActivity': 'economicActivity',
            'company': 'company',
            'profession': 'profession',
        }
        
        