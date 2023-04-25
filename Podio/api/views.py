from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from Podio.models import Podio
from Podio.api.serializers import PodioSerializer


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
        serializer = PodioSerializer(podio, data=request.data)

        if (serializer.is_valid(raise_exception=True)):

            serializer.save()

            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
