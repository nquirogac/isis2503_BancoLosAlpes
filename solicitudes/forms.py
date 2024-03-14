from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'userId',
            'operation',
            'created_at'
        ]

        labels = {
            'userId': 'User ID',
            'operation': 'Operation',
            'created_at': 'Created At'
        }
