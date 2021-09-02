from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.http import request


class UserRegisterForm(UserCreationForm): #hereda de UserCreation
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields }

class editProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = {
        "username",
        "email"
        }