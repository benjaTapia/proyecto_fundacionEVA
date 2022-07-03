from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here. 

#Modelo Aportador
class Aportador(models.Model):
    idAportador = models.IntegerField(primary_key=True, verbose_name="Id aportador")
    nombreAportador = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre")
    apellidoAportador = models.CharField(max_length=80, blank=False, null=False, verbose_name="Apellido Aportador")
    rutAportador = models.CharField(max_length=15, blank=False, null=False, verbose_name="Rut")
    usuarioAportador = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nombre de Usuario")
    passAportador = models.CharField(max_length=30, blank=False, null=False, verbose_name="Contraseña")
    correoAportador = models.CharField(max_length=30, blank=False, null=False, verbose_name="Correo Electrónico")

    def __str__(self):
        return self.nombreAportador

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12,blank=False, null=False, verbose_name="Rut")

#Modelo Aporte
class Aporte(models.Model):
    idAporte = models.IntegerField(primary_key=True, verbose_name="Id Aporte")
    idAportador = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Nombre Aportador :")
    montoAporte = models.IntegerField(null=False, blank=False, verbose_name="Monto de Aporte :") 
    tarjetaAporte = models.CharField(max_length=16, blank=False, null=False, verbose_name="Tarjeta de Aporte :")
    fechaAporte = models.DateTimeField(null=False, blank=False, verbose_name="Fecha del Aporte (Debe ser desde mañana en adelante) :")
    frecuenciaAporte = models.BooleanField(null=False, blank=False, verbose_name="¿Aporte mensual?")

    def __int__(self):
        return self.idAporte