from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views import View

urlpatterns = [
    path('login/', LoginView.as_view(template_name= 'cuentas/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name= 'register'),
    path("perfil/", views.perfil, name="perfil"),
    path("editarPerfil/", views.editarPerfil, name="editarPerfil"),
    path("password/", PasswordChangeView.as_view(
        template_name = "cuentas/cambiar_pass.html",
        success_url = reverse_lazy("login")), name="change_password"),
] 