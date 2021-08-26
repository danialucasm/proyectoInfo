from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method =='POST': #Para utilizar los campos que fueron llenados en el form, else para q se muetre form vacio
        form = UserRegisterForm(request.POST) #para acceder a la info
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username'] 
            messages.success(request, f'Usuario {username} creado')
            return redirect('login') #como ya se registro ahora se tiene que ir a loguear
    else: 
        form = UserRegisterForm()
        context = {'form' : form}
        return render(request, 'myapp/register.html', context) #para que se mantenga en register

def perfil(request):
    return render(request, 'myapp/perfil.html')