from rest_framework import serializers

from Persona.models import *


class PersonaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Persona
        # fields = '__all__'
        exclude = ('foto',)


class VoluntarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Voluntario
        fields = ['experiencia']


class PersonaSerializerView(serializers.ModelSerializer):

    class Meta:

        model = Persona
        fields = ['tipo_documento', 'numero_documento', 'nombre', 'apellido', 'fecha_nacimiento', 'genero', 'telefono']


class NiñoSerializerView(serializers.ModelSerializer):
    persona = PersonaSerializerView()

    class Meta:

        model = Niño
        fields = '__all__'


class VoluntarioSerializerView(serializers.ModelSerializer):
    persona = PersonaSerializerView()

    class Meta:

        model = Voluntario
        fields = '__all__'
