from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegisterForm, editProfileForm
from django.contrib import messages


# Create your views here.

def register(request):
    form = UserRegisterForm()
    if request.method =='POST': #Para utilizar los campos que fueron llenados en el form, else para q se muestre form vacio
        form = UserRegisterForm(request.POST) #para acceder a la info
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username'] 
            messages.success(request, f'Usuario {username} creado')
            return redirect('login') #como ya se registro ahora se tiene que ir a loguear

    context = {'form' : form}
    return render(request, 'cuentas/register.html', context)

def perfil(request):
    return render(request, 'cuentas/perfil.html')

def editarPerfil(request):
    if not request.user.is_authenticated:
        return redirect("login")
    perfil = request.user
    form = editProfileForm(instance=perfil)
    if request.method == "POST":
        form = editProfileForm(request.POST, instance=perfil)
        if form.is_valid():
            user = form.save()
            return redirect("perfil")
    context = {"form":form}
    return render(request, 'cuentas/editarPerfil.html', context)
