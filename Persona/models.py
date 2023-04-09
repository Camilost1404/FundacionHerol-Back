from django.db import models
from django.core.validators import FileExtensionValidator


class Persona(models.Model):
    """
    Clase para la creación del modelo de la Persona.
    """

    class Genero(models.TextChoices):
        """
        Clase anidada para establecer las opciones del campo género.
        """
        MASCULINO = 'Masculino',
        FEMENINO = 'Femenino',
        OTRO = 'Otro'

    class TipoDocumento(models.TextChoices):
        """
        Clase anidada para establecer las opciones del campo tipo de documento.
        """
        CC = 'Cédula de Ciudadanía'
        RC = 'Registro Civil'
        TI = 'Tarjeta de Identidad'
        CE = 'Cédula de Extranjería'
        NIT = 'Número de Identificación Tributaria'

    # Campos del modelo
    numero_documento = models.CharField(max_length=18, primary_key=True)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80, null=True, blank=False)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=False)
    genero = models.CharField(max_length=15, choices=Genero.choices, null=True, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=False)
    telefono = models.CharField(max_length=12, null=True, blank=False)
    foto = models.ImageField(upload_to='image/', max_length=255, null=True, blank=False, validators=[FileExtensionValidator(['jpg', 'png'])])
    tipo_documento = models.CharField(max_length=50, choices=TipoDocumento.choices)

class Niño(models.Model):
    """
    Clase para la creación del modelo de Niño.
    """

    # Campos del modelo
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Voluntario(models.Model):
    """
    Clase para la creación del modelo de Voluntario.
    """

    # Campos del modelo
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    estado = models.BooleanField(default=0)
    experiencia = models.CharField(max_length=150)