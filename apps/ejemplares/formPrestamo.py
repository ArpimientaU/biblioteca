from django import forms
from apps.ejemplares.models import Prestar

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestar
        fields = [
            'usuario',
            'ejemplar',
            'fecha_prestamo',
            'fecha_devolucion',
        ]

        labels = {
            'usuario':'Elija el usuario',
            'ejemplar':'Elija el ejemplar',
            'fecha_prestamo': 'Ingrese la fecha del prestamo',
            'fecha_devolucion':'Ingrese la fecha de la devolucion',
        }

        widgets ={
            'fecha_prestamo': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_devolucion': forms.DateInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'ejemplar': forms.Select(attrs={'class': 'form-control'}),
        }