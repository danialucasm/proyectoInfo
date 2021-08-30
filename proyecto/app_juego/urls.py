from django.urls import path
from . import views

urlpatterns = [

    path("", views.principal, name="principal"),
    path("inicio/", views.inicio, name="inicio"),
    path("instrucciones/", views.instrucciones, name="instrucciones"),
    path("jugar/", views.jugar, name="jugar"),
    path("tablero/", views.tablero, name="tablero"),
    path("resultado/<int:pregunta_respondida_pk>/", views.resultado_pregunta, name="resultado"),

] 