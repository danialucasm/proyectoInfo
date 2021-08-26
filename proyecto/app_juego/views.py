from django.shortcuts import render

# Create your views here.

def inicio(request):
    context = {}
    return render(request, 'app_juego/inicio.html', context)

def principal(request):
    if (request.user.is_authenticated and request.user.is_staff):
        template ='app_juego/admin_dashboard.html' #cambiar porque no anda
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
