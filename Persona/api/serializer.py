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
        exclude =('numero_documento',)

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

class NiñoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Niño
        fields = ['persona_id']