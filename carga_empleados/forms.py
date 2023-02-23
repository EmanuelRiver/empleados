from django import forms

class EmpleadosFormularios(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    cargo=forms.CharField()