from django import forms
from django.forms import ModelForm, fields, Form
from .models import Aportador, Aporte
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AporteForm(ModelForm):
    class Meta:
        model = Aporte
        fields = ['idAportador','montoAporte','tarjetaAporte','fechaAporte','frecuenciaAporte']

class AgregarAportadorForm(UserCreationForm):
    rut = forms.CharField(max_length=12, required=True, label="Rut")
    class Meta:
        model = User
        fields = ['username', 'rut', 'first_name', 'last_name', 'email']

class IniciarSesionForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']

class RegistroForm(ModelForm):
    class Meta:
        model = Aportador
        fields = ['rutAportador','nombreAportador', 'apellidoAportador','usuarioAportador', 'correoAportador', 'passAportador']

class FechasForm(forms.Form):
    fechaInicio = forms.DateField(label="Fecha Inicio")
    fechaFin = forms.DateField(label="Fecha Fin")

