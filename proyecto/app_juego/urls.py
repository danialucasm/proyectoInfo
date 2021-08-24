# from django.contrib import admin
from django.urls import path
# from django.urls import include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.principal, name="principal"),
    path("inicio/", views.inicio, name="inicio"),
    path("perfil/", views.perfil, name="perfil"),
    path("instrucciones/", views.instrucciones, name="instrucciones"),

] 