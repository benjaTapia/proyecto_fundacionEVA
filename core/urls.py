from operator import index
from unicodedata import name
from django.urls import path
from .views import index, iniciarSesion, poblar_Aportador, agregarAportes, historialAportes, registroAportador, salirCuenta, plantilla, editarAportes
from apirest.apiAportador import apiAportador

urlpatterns = [
    path('', index, name="index"),
    path('poblar_Aportador',poblar_Aportador, name="poblar_Aportador"),
    path('aportes/<id>', agregarAportes, name="agregarAportes"),
    path('registroAportador',registroAportador, name="registroAportador"),
    path('historialAportes/<id>/<action>', historialAportes, name="historialAportes"),
    path('iniciarSesion',iniciarSesion, name="iniciarSesion"),
    path('salirCuenta',salirCuenta, name="salirCuenta"),
    path('plantilla',plantilla, name="plantilla"),
    path('editarAportes/<id>/<idAporte>',editarAportes,name="editarAportes"),
    #API REST
    path('apirest/registroForm', apiAportador.registroForm)
]