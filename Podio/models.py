from django.db import models
from Persona.models import Persona

# Create your models here.


class Podio(models.Model):
    
    class TipoPodio(models.TextChoices):
        """
        Clase anidada para establecer las opciones del campo tipo de documento.
        """
        PN = 'Podio Niño'
        PP = 'Podio Persona'
        PE = 'Podio Empresa'
        PI = 'Podio Internacional'

    tipo_podio = models.CharField(max_length=50, choices=TipoPodio.choices, null=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
