from rest_framework import serializers

from Persona.api.serializer import PersonaSerializerView
from Podio.models import Podio


class PodioSerializer(serializers.ModelSerializer):

    persona = PersonaSerializerView()

    class Meta:

        fields = '__all__'
        model = Podio