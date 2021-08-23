from django.conf.urls import url
from django.urls import path
from django.conf import settings
#from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.feed, name='feed'),
    path('login/', LoginView.as_view(template_name= 'myapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'myapp/logout.html'), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('register/', views.register, name= 'register'),
    
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)