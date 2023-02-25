from django import forms

class EmpleadosFormularios(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    cargo=forms.CharField()

class EmpresaFormularios(forms.Form):
    nombre = forms.CharField()
    razon_social = forms.CharField()
    cuit = forms.IntegerField()

class VehiculoFormularios(forms.Form):
    marca=forms.CharField()
    modelo=forms.CharField()
    patente=forms.CharField()
    