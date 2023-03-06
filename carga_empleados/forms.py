from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
