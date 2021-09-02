from django.core.management import BaseCommand
from app_juego.models import Pregunta, ElegirRespuesta
from csv import DictReader


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("./preguntas.csv", 'r') as archivo:
            for fila in DictReader(archivo):
                preg = Pregunta()
                preg.texto = fila["texto"]
                preg.max_puntaje = fila["puntaje"]
                preg.save()                
                res_correcta = ElegirRespuesta ()
                res_2 = ElegirRespuesta ()
                res_3 = ElegirRespuesta ()

                res_correcta.correcta = True
                res_correcta.pregunta = preg
                res_correcta.texto = fila["opcion_correcta"]
                res_correcta.save()

                res_2.pregunta = preg
                res_2.texto = fila["opcion2"]
                res_2.save()
                res_3.pregunta = preg
                res_3.texto = fila["opcion3"]
                res_3.save()


                