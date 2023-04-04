from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class Persona(models.Model):

    class Genero(models.TextChoices):

        MASCULINO = 'Masculino',
        FEMENINO = 'Femenino',
        OTRO = 'Otro'

    class TipoDocumento(models.TextChoices):

        CC = 'Cédula de Ciudadanía'
        RC = 'Registro Civil'
        TI = 'Tarjeta de Identidad'
        CE = 'Cédula de Extranjería'
        NIT = 'Número de Identificación Tributaria'

    numero_documento = models.CharField(max_length=18, primary_key=True)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    genero = models.CharField(max_length=15, choices=Genero.choices, null=True, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=False)
    telefono = models.CharField(max_length=12, null=True, blank=False)
    foto = models.ImageField(upload_to='image/', max_length=255, null=True, blank=False, validators=[FileExtensionValidator(['jpg', 'png'])])
    tipo_documento = models.CharField(max_length=50, choices=TipoDocumento.choices)


class Niño(models.Model):

    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Voluntario(models.Model):

    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    experiencia = models.CharField(max_length=150)