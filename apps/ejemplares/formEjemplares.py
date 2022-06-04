from django import forms
from apps.ejemplares.models import Ejemplar

class EjemplaresForm(forms.ModelForm):
    class Meta:
        model = Ejemplar
        fields = [
            'libro',
            'localizacion',
        ]

        labels = {
            'libro':'Seleccione un libro',
            'localizacion':'Ingrese la localizacion',
        }

        widgets ={
            'localizacion': forms.TextInput(attrs={'class': 'form-control'}),
            'libro': forms.Select(attrs={'class': 'form-control'}),
        }