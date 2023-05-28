from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from User.models import *
from User.api.serializers import *


class ViewUser(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = UserViewSerializer(user, many=True)
        return Response(serializer.data)


class DeleteUser(APIView):
    def delete(self, request):
        id_user = request.query_params['id_user']
        user = User.objects.get(id=id_user)
        email = user.email
        user.delete()
        return Response('Usuario ' + email + ' eliminado con exito', status=status.HTTP_200_OK)


class UserCreate(APIView):
    @transaction.atomic
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Usuario creado con exito', status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserEspecifico(APIView):

    def get(self, request):
        id_user = request.query_params['id_user']
        user = User.objects.get(id=id_user)
        serializer = UserViewSerializer(user)
        return Response(serializer.data)


class ModificarUser(APIView):
    def patch(self, request):
        id_user = request.query_params['id_user']
        user = User.objects.get(id=id_user)
        serializer = UserUpdateSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Usuario modificado con exito', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSuperEstado(APIView):

    def put(self, request):
        id_user = request.query_params['id_user']
        user = User.objects.get(id=id_user)
        print(request.data)
        if 'is_superuser' in request.data:
            serializer = UserUpdateEstadoSerializer1(user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response('Usuario modificado con exito', status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserActiveEstado(APIView):

    def put(self, request):
        id_user = request.query_params['id_user']
        user = User.objects.get(id=id_user)
        if 'is_active' in request.data:
            serializer = UserUpdateEstadoSerializer(user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response('Usuario modificado con exito', status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
