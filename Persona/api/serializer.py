from rest_framework import serializers

from Persona.models import *


class PersonaSerializerView2(serializers.ModelSerializer):
    class Meta:

        model = Persona
        fields = '__all__'


class PersonaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Persona
        # fields = '__all__'
        exclude = ('foto',)


class NiñoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Persona
        # fields = '__all__'
        exclude = ('email',)

    def validate_nombre(self, value):
        # Aplicar capitalización al nombre
        return value.lower().capitalize()

    def validate_apellido(self, value):
        # Aplicar capitalización y conversión a minúsculas al apellido
        return value.lower().capitalize()


class VoluntarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Voluntario
        fields = ['experiencia']


class PersonaSerializerView(serializers.ModelSerializer):

    class Meta:

        model = Persona
        fields = ['tipo_documento', 'numero_documento', 'nombre',
                  'apellido', 'fecha_nacimiento']


class NiñoPodioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Persona
        fields = ['tipo_documento', 'numero_documento',
                  'apellido', 'fecha_nacimiento', 'nombre', 'foto']


class NiñoSerializerUpdate(serializers.ModelSerializer):

    class Meta:

        model = Persona
        exclude = ('numero_documento', 'nombre')


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


class VoluntarioEspecificoSerializerView(serializers.ModelSerializer):
    persona = PersonaSerializerView2()

    class Meta:

        model = Voluntario
        fields = '__all__'


class VoluntarioEstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voluntario
        fields = ['estado']


class VoluntarioFotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = ['foto']
