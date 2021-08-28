from django.core.exceptions import ObjectDoesNotExist
from .models import TriviaUsuario, Pregunta, PreguntasRespondidas
from django.contrib.admin.sites import AdminSite
from django.shortcuts import redirect, render
from django.http.response import Http404
# Create your views here.


def inicio(request):
    context = {}
    return render(request, 'app_juego/inicio.html', context)


def jugar(request):
    TriviaUser, created = TriviaUsuario.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = TriviaUsuario.intentos.select_releated('pregunta').get(pregunta_pk=pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')

        try:
            opcion_seleccionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
        except ObjectDoesNotExist:
            raise Http404
        TriviaUser.validar_intento(pregunta_respondida,opcion_seleccionada)
        return redirect(pregunta_respondida)
    else:
        pregunta = TriviaUser.obtener_nuevas_preguntas()        
        if pregunta is not None:
            TriviaUser.crear_intentos(pregunta)

        context= {
            'pregunta':pregunta
        }
    return render (request,'app_juego/juego.html', context)
 

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

   