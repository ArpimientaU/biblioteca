from django import forms
from apps.libros.models import Libro

class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'titulo',
            'editorial',
            'numero_pagina',
            'isbn',
            'autor',
        ]

        labels = {
            'titulo':'Ingrese el titulo',
            'editorial':'Ingrese el número de páginas que posee',
            'numero_pagina':'Ingrese la editorial',
            'isbn':'Ingrese el ISBN del libro',
            'autor':'Seleccione el autor',
       }

        widgets ={
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_pagina': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
        }