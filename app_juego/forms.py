from  django import forms
from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas
# from  django.contrib.auth.forms import UserCreationForm
# from  django.contrib.auth import  authenticate, get_user_model


class ElegirInLineFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(ElegirInLineFormset, self).clean()

        respuesta_correcta = 0
        for formulario in self.forms:
            if not formulario.is_valid(): 
                return

            if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
                respuesta_correcta += 1 #actualizamos respuesta

        try:
            assert respuesta_correcta == Pregunta.NUMER_RESPUESTAS_PERMITIDAS #Control entre respuesta y las permitidas
        except AssertionError:
            raise forms.ValidationError('Solo una respuesta es permitida como correcta, vuelva a intentarlo') #solo puede registrar UNA sola correcta