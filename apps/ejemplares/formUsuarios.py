from django import forms
from apps.ejemplares.models import Usuario

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido',
            'direccion',
            'telefono',
        ]

        labels = {
            'nombre':'Ingrese los nombres',
            'apellido':'Ingrese los apellidos',
            'direccion':'Ingrese la dirección',
            'telefono':'Ingrese el teléfono',
       }

        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }