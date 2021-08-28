from django.contrib.admin.sites import AdminSite
from django.shortcuts import redirect, render

# Create your views here.

def inicio(request):
    context = {}
    return render(request, 'app_juego/inicio.html', context)

def principal(request):
    if (request.user.is_authenticated and request.user.is_staff):
        return redirect("admin/", AdminSite.urls) #site de administrador
    else:
        template = 'app_juego/principal.html'
        context = {}
        return render(request,template, context)

def instrucciones(request):
    context = {}
    return render(request,'app_juego/instrucciones.html', context)

def perfil(request):
    context = {}
    return render(request,'app_juego/perfil.html', context)
