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
