from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from Persona.api.serializer import *
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

    def get(self, request):
        niños = Niño.objects.all()
        serializer = NiñoSerializerView(niños, many=True)
        return Response(serializer.data)


class VoluntarioView(APIView):

    def get(self, request):
        voluntario = Voluntario.objects.all()
        serializer = VoluntarioSerializerView(voluntario, many=True)
        return Response(serializer.data)


class GuardarNiño(APIView):
    @transaction.atomic
    def post(self, request):

        serializer = NiñoSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            persona = serializer.save()
            serializer2 = NiñoCreateSerializer(data=request.data)
            if serializer2.is_valid(raise_exception=True):
                serializer2.save(persona=persona)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BorrarNiño(APIView):
    def delete(self, request):
        id_niño = request.query_params['id_niño']
        persona = Persona.objects.filter(numero_documento=id_niño)
        persona.delete()
        return Response('Niño con id {id_niño} eliminado')


class modificarNiño(APIView):
    def put(self, request):
        id_niño = request.query_params['id_niño']
        persona = Persona.objects.get(numero_documento=id_niño)
        serializer = NiñoSerializerUpdate(persona, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NiñoEspecificoView(APIView):

    def get(self, request):
        id_niño = request.query_params['id_niño']
        niño = Persona.objects.get(numero_documento=id_niño)
        serializer = PersonaSerializerView2(niño)
        return Response(serializer.data)


class VoluntarioEspecifico(APIView):
    def get(self, request):
        id_voluntario = request.query_params['id_voluntario']
        voluntario = Voluntario.objects.get(persona_id=id_voluntario)
        serializer = VoluntarioEspecificoSerializerView(voluntario)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BorrarVoluntario(APIView):
    def delete(self, request):
        id_voluntario = request.query_params['id_voluntario']
        persona = Persona.objects.filter(numero_documento=id_voluntario)
        persona.delete()
        return Response('Voluntario con documento '+id_voluntario+' eliminado')


class EstadoVoluntario(APIView):
    def patch(self, request):
        id_voluntario = request.query_params['id_voluntario']
        persona = Voluntario.objects.get(persona_id=id_voluntario)
        if not persona.estado:
            data = {'estado': 1}
            serializer = VoluntarioEstadoSerializer(persona, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Error', status=status.HTTP_403_FORBIDDEN)

class ModificarVoluntario(APIView):
    @transaction.atomic
    def put(self,request):
        id_voluntario = request.query_params['id_voluntario']
        voluntario = Persona.objects.get(numero_documento = id_voluntario)
        serializer = VoluntarioFotoSerializer(voluntario,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Voluntario modificado con exito', status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
