from logging import exception
from time import timezone
from turtle import home
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Aportador, Aporte, PerfilUsuario
from .forms import AporteForm, FechasForm, RegistroForm, AgregarAportadorForm, IniciarSesionForm
from datetime import datetime, timedelta, time

# Create your views here.

#-------------------------------------------------------------------
#----------------------Funciones sin ID-----------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------

def plantilla(request):
    return render(request,"core/plantilla.html")
##Función del index
def index(request):
    data = {"form": IniciarSesionForm()}
    try:
        list = User.objects.all()
        data = {"list": list}
    except:
        pass
    return render(request, "core/plantilla.html", data)

##Función del registro
def registroAportador(request):
    data = {"form" : AgregarAportadorForm}
    if request.method == "POST":
        form = AgregarAportadorForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            rutUsuario = request.POST.get("rut")
            PerfilUsuario.objects.update_or_create(user = usuario, rut = rutUsuario)
            data["mesg"] = "Se ha logrado registrar"
        else:
            data["mesg"] = "Ha ocurrido un error, intentelo más tarde"
            
    return render(request, "core/registro.html", data)

##Función del inicio de sesión
def iniciarSesion(request):
    data = {"mesg": "", "form": IniciarSesionForm()}
    if request.method == "POST":
        form = IniciarSesionForm(request.POST)
        if form.is_valid:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(agregarAportes, user.id)
                else:
                    data["mesg"] = "El usuario o la contraseña no son correctos"
            else:
                data["mesg"] = "El usuario o la contraseña no son correctos"
    return render(request, "core/inicioSesion.html", data)

##Función Logout
def salirCuenta(request):
    logout(request)
    return redirect(index)
#-------------------------------------------------------------------
#----------------------Funciones con ID-----------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------

##Agregar un aporte
def agregarAportes(request, id):
    ##Valida que haya iniciado sesión --> Busca el user del REQUEST, es decir, busca que se haya iniciado sesión, lo que de 
    ##                                    ahora en adelante viaja en el request, si no está auntenticado (No inicia sesión, o no
    ##                                    se encuentra, devuelve al index, si no, que actue con normalidad)  
    #if not request.user.is_authenticated:
    #    return redirect(index)
    
    #Obtiene los objetos para el usuario
    try:
        #object = User.objects.get(id = request.user.id) --> También trabaja y encuentra la ID, ya que está con sesión INICIADA, si no
        #                                                    entonces te tira al index
        object = User.objects.get(id = id)
        data = {"aportador" : object, "form": AporteForm, "id":id}
    except:
        return redirect(index)
    
    #Intenta agregar un aporte
    if request.method == "POST":
        form= AporteForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit = False)
            model_instance.save()
            data["mesg"] = "Se ha logrado guardar su aporte"
        else:
            data["mesg"] = "Hubo un error, por favor, intentelo más tarde"

    return render(request, "core/agregarAportes.html", data)

##Historial de usuarios
def historialAportes(request, id, action):
    ##Valida que haya iniciado sesión
    #if not request.user.is_authenticated:
    #    return redirect(index)

    data = {"form" : FechasForm, "id":id, "action" : action}

    #Se crean los objetos del usuario, para pedir los datos
    object = User.objects.get(id = id)
    perfil = PerfilUsuario.objects.get(user = object)
    data["aportador"] = object
    data["perfil"] = perfil

    #Trabajar con la fecha de hoy, para luego ver si es antes o despues
    hoyR = datetime.now()
    hoyR = hoyR.replace(hour=00, minute=00, second=00)
    hoyR = str(hoyR)

    #Si el usuario busca su historial, es decir, usa la accion "his", hará los calculos para ver aportes hacia el pasado
    if action == "his":
        ##Para buscar las fechas pedidas por EL USUARIO
        if request.method == "POST":
            fechaInicio = request.POST.get("fechaInicio")
            fechaFin = request.POST.get("fechaFin")
            list = Aporte.objects.filter(fechaAporte__range=(fechaInicio, fechaFin)).filter(idAportador = id)
            data["list"] = list
        ##Para buscar por fechas pasadas hasta el 2000
        else:
            list = Aporte.objects.filter(fechaAporte__lte=(hoyR)).filter(idAportador = id)
            data["list"] = list

    #Si el usuario busca sus aportes a futuro, es decir, usa la accion "fut", hará los calculos para ver aportes hacia adelante
    elif action == "fut":
        ##Para buscar las fechas pedidas por EL USUARIO
        if request.method == "POST":
            fechaInicio = request.POST.get("fechaInicio")
            fechaFin = request.POST.get("fechaFin")
            list = Aporte.objects.filter(fechaAporte__range=(fechaInicio, fechaFin)).filter(idAportador = id)
            data["list"] = list
        ##Para buscar por fechas pasadas hasta el 2000
        else:
            list = Aporte.objects.filter(fechaAporte__gt=(hoyR)).filter(idAportador = id)
            data["list"] = list
    return render(request, "core/historialAportes.html", data) 

##Agregar un aporte
def editarAportes(request, id, idAporte):
    object = User.objects.get(id = id)
    aporteobj = Aporte.objects.get(idAporte = idAporte)
    data = {"aportador" : object, "form": AporteForm, "id":id, "idAporte":idAporte, "aporte":aporteobj}

    #Intenta agregar un aporte
    if request.method == "POST":
        form = AporteForm(request.POST, instance=aporteobj)
        if form.is_valid():
            form.save()
            data["mesg"] = "Se ha logrado guardar su aporte"
        else:
            data["mesg"] = "Hubo un error, por favor, intentelo más tarde"
    data["form"] = AporteForm(instance=aporteobj)

    return render(request, "core/editarAportes.html", data)


###FUNCIÓN A TRABAJAR CON MUCHO CUIDADO, SOLO REUTILIZAR PARA POBLAR LA DB; LUEGO BORRAR LOS ACCESOS DESDE OTRAS PÁGINAS.
###ESTA ES LA FUNCIÖN QUE INCLUSO PUEDE JODER EL PROGRAMA, CUIDADO CON ESTO 

def poblar_Aportador(request):
    #Users, cambiar el username y rut al crearlo

    #User.objects.create(first_name = "Juan", last_name = "Peroz", username = "JuPeroz", password = "JP1234##", email = "jperoz@mail.com")
    #User.objects.create(first_name = "Juan", last_name = "Periz", username = "PerizJJ", password = "JP1234##", email = "jperiz@mail.com")
    #PerfilUsuario.objects.create(user = User.objects.get(id=3), rut="21-k")
    #PerfilUsuario.objects.create(user = User.objects.get(id=4),rut="20-k")

    #Aportes, cambiar el id para el user.objects, seguir el mismo formato de fecha

    #Aporte.objects.create(idAportador = User.objects.get(id=2), montoAporte = 1500 , tarjetaAporte = 1234123412341234, fechaAporte = "2022-05-15 00:00:00", frecuenciaAporte= True)
    #Aporte.objects.create(idAportador = User.objects.get(id=2), montoAporte = 1500 , tarjetaAporte = 1234123412341234, fechaAporte = "2022-05-16 00:00:00", frecuenciaAporte= True)
    #Aporte.objects.create(idAportador = User.objects.get(id=2), montoAporte = 1500 , tarjetaAporte = 1234123412341234, fechaAporte = "2022-05-17 00:00:00", frecuenciaAporte= True)

    #Volver al index, donde normalmente se invocaría
    return redirect(index)
    #Aporte.objects.create(IdAportador = , montoAporte = , tarjetaAporte = , fechaAporte = , frecuenciaAporte= )