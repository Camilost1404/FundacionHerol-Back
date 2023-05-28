from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from Podio.models import Podio
from Persona.models import Niño
from Podio.api.serializers import PodioSerializer, NiñoDocumSerializer


class AllPodiosView(APIView):

    def get(self, request):

        podios = Podio.objects.all()

        serializer = PodioSerializer(podios, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PodioView(APIView):

    def get(self, request, id):

        podio = Podio.objects.get(id=id)

        serializer = PodioSerializer(podio)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def put(self, request, id):

        podio = Podio.objects.get(id=id)

        # Actualizar el campo persona_id en el objeto podio
        podio.persona_id = request.data.get('persona')

        podio.save()

        serializer = PodioSerializer(podio)

        return Response(serializer.data, status=status.HTTP_200_OK)


class DocumentoNiños(APIView):
    def get(self, request):
        niños = Niño.objects.all()
        serializer = NiñoDocumSerializer(niños, many=True)
        return Response(serializer.data)
