from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from User.models import *
from User.api.serializers import *

from django.core.mail import send_mail


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


class EmailContacto(APIView):

    def post(self, request):

        asunto = request.data['asunto']
        email = request.data['email']
        mensaje = request.data['mensaje']

        # Configurar los detalles del correo electrónico
        email_subject = f'Contacto: {asunto}'
        email_message = f'De: {email}\n\n{mensaje}'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['camilost1408@gmail.com']

        try:
            # Enviar el correo electrónico
            send_mail(email_subject, email_message, from_email, to_email)

            # Enviar una respuesta JSON exitosa a la solicitud de React
            return Response({'success': 'Mensaje enviado con éxito - Pronto nos pondremos en contacto contigo'}, status=status.HTTP_200_OK)

        except:
            # En caso de error, enviar una respuesta JSON con el mensaje de error
            return Response({'error': 'Error al enviar el mensaje'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAuth(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):

        serializer = UserSerializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
