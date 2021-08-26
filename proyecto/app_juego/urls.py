from django.urls import path
from . import views

urlpatterns = [

    path("", views.principal, name="principal"),
    path("inicio/", views.inicio, name="inicio"),
    path("instrucciones/", views.instrucciones, name="instrucciones"),
    path("perfil/", views.perfil, name="perfil"),
] 