from django.db import models

from Persona.models import Persona
# Create your models here.


class Donante(models.Model):
    """
    Clase para la creación del modelo de Donante.
    """

    # Campos del modelo
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)


class Donacion(models.Model):
    """
    Clase para la creación del modelo de Donacion.
    """

    donante = models.ForeignKey(Donante, on_delete=models.CASCADE)
    valor = models.FloatField()
    fecha_donacion = models.DateTimeField(auto_now_add=True)
    moneda = models.CharField(max_length=4, default='cop')
