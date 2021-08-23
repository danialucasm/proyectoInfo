from collections import defaultdict
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
#----------------------------MODELOS PARA ADMINISTRACION
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #image
    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default= timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}' #Muestro que es cada cosa


