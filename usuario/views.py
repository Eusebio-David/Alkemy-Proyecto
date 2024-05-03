from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.db import IntegrityError
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.messages import constants as messages




# Create your views here.

def crear_usuario(request):
    if request.method == 'GET':
        return render(request, 'usuario/registro_usuario.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #si las contraseñas son coincidentes registramos el usuario
            try:
                usuario = User.objects.create_user(username=request.POST['username'],
                                                   password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('compra:index')
            
            except IntegrityError:
                return render(request, 'usuario/registro_usuario.html',{
                    'form': UserCreationForm,
                    'error': "El usuario ingresado ya existe."
                })
        else:
            return render(request, 'usuario/registro_usuario.html', {
                'form': UserCreationForm,
                'error': "Las contraseñas no coiciden."
            })

#Funcion para ingresar al sistema
def login_view(request):
    if request.method == 'GET':
        return render(request, 'usuario/login.html', {
            'form': AuthenticationForm
        })
    else:
        try:
            usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if usuario is None:
                return render(request, 'usuario/login.html',{
                    'form': AuthenticationForm,
                    'error': "Usuario o contraseña incorrecto."
                })
            else:
                login(request, usuario)
                return redirect('compra:index')
       
       
        except :
            return render(request, 'usuario/login.html',{
                'form': AuthenticationForm,
                'error': "El Usuario o Contraseña no Existe"
            })
        



def logout_view(request):
    logout(request)
    return redirect(reverse('compra:index'))