from django import forms
from .models import Cita, Horario, Servicio

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre_cliente', 'telefono', 'servicio', 'fecha', 'hora']
        widgets = {
            'servicio': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'border rounded p-2 w-full'}),
            'hora': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
            'nombre_cliente': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'telefono': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
        }

