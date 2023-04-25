from django.db import models
from Persona.models import Persona

# Create your models here.


class Podio(models.Model):

    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
