from rest_framework import serializers

from Donante.models import *

class DonanteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donante
        fields = ['persona_id']

class DonacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donacion
        fields = ['valor', 'moneda']