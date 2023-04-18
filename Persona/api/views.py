from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from datetime import datetime

from Persona.api.serializer import VoluntarioSerializer, PersonaSerializer, NiñoSerializerView, VoluntarioSerializerView
from Persona.models import *


class RegisterVoluntarioView(APIView):

    @transaction.atomic
    def post(self, request):

        serializer_voluntario = VoluntarioSerializer(data=request.data)

        if serializer_voluntario.is_valid(raise_exception=True):

            # Crear un objeto ModelB con el nombre y apellido proporcionados y guardar en la base de datos.
            persona, created = Persona.objects.get_or_create(
                numero_documento=request.data['numero_documento'],
                defaults={
                    'nombre': request.data['nombre'],
                    'apellido': request.data['apellido'],
                    'tipo_documento': request.data['tipo_documento'],
                    'email': request.data['email'],
                    'genero': request.data['genero'],
                    'telefono': request.data['telefono'],
                    'fecha_nacimiento': request.data['fecha_nacimiento'],
                }
            )

            if not created:
                serializer_persona = PersonaSerializer(
                    persona, data=request.data)

                if serializer_persona.is_valid(raise_exception=True):

                    persona = serializer_persona.save()

            voluntario = Voluntario(
                persona=persona, experiencia=request.data['experiencia'])

            # Si la persona ya tiene un voluntario asociado, retornar un error
            if voluntario.persona:
                return Response({"error": "Voluntario ya se encuentra registrado - Por favor contactese con nosotros"}, status=status.HTTP_400_BAD_REQUEST)

            voluntario.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer_voluntario.errors + serializer_persona.errors, status=status.HTTP_400_BAD_REQUEST)


class NiñoView(APIView):

    def get(self,request):
        niños = Niño.objects.all()
        serializer = NiñoSerializerView(niños, many=True)
        return Response(serializer.data)

class VoluntarioView(APIView):

    def get(self,request):
        voluntario = Voluntario.objects.all()
        serializer = VoluntarioSerializerView(voluntario, many = True)
        return Response(serializer.data)       