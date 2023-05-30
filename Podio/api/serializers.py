from rest_framework import serializers

from Persona.api.serializer import NiñoPodioSerializer
from Podio.models import Podio
from Persona.models import Niño

class PodioSerializer(serializers.ModelSerializer):

    persona = NiñoPodioSerializer()

    class Meta:

        fields = '__all__'
        model = Podio


class NiñoDocumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niño
        fields = ['persona_id']
