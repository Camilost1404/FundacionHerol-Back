from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from Persona.models import Persona
from Donante.api.serializers import *

import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY


class RealizarDonacion(APIView):
    def post(self, request):

        datos_formulario = request.data

        precio = request.data['precio']
        email = request.POST.get('email')
        moneda = request.POST.get('moneda')

        line_item = {
            "price_data": {
                "currency": moneda,
                "unit_amount": int(precio) * 100,
                "product_data": {
                    "name": 'Donacion',
                },
            },
            "quantity": 1,

        }

        checkout_session = stripe.checkout.Session.create(
            customer_email=email,
            payment_method_types=["card"],
            line_items=[line_item],
            mode="payment",
            success_url='http://localhost:5173/pago_exitoso',
            cancel_url='http://localhost:5173/pago_rechazado',
            payment_intent_data={
                'metadata': datos_formulario
            }
        )

        # requests.post(webhook_url, json=payload)

        return Response({'id': checkout_session.url})


class DonanteRegister(APIView):

    @transaction.atomic
    def post(self, request):

        payload = request.body
        event = None

        try:
            event = stripe.Event.construct_from(
                json.loads(payload), stripe.api_key
            )
        except ValueError as e:
            # Error al decodificar el JSON
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Manejar el evento de pago exitoso
        if event.type == 'payment_intent.succeeded' or event.type == 'checkout.session.async_payment_succeeded':
            session = event.data.object

            print(session)

            metadata = session.metadata
            # Guardar los datos en tu modelo o realizar otras operaciones necesarias

            # Crear un objeto con el nombre y apellido proporcionados y guardar en la base de datos.
            persona, created = Persona.objects.get_or_create(
                numero_documento=metadata['numero_documento'],
                defaults={
                    'nombre': metadata['nombre'],
                    'apellido': metadata['apellido'],
                    'tipo_documento': metadata['tipo_documento'],
                    'email': metadata['email'],
                    'telefono': metadata['telefono'],
                    'foto': 'image/DEFAULT.png'
                }
            )

            if created:
                persona.save()

            serializer2 = DonanteCreateSerializer(data=metadata)

            if serializer2.is_valid(raise_exception=True):

                donante = serializer2.save(persona=persona)

                serializer3 = DonacionSerializer(data=metadata)

                if serializer3.is_valid(raise_exception=True):

                    serializer3.save(donante=donante)

                    return Response(status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer3.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


class VerDonacion(APIView):

    def get(self, request):
        donaciones = Donacion.objects.select_related('donante').all()
        dict = []
        for donacion in donaciones:
            dict2 = {}
            persona = donacion.donante.persona
            num_doc = persona.numero_documento
            donador = Persona.objects.filter(numero_documento=num_doc).values_list(
                'numero_documento', 'nombre', 'apellido', 'email')
            c = donador[0]
            dict2['numero_documento'] = num_doc
            dict2['nombre'] = c[1]
            dict2['apellido'] = c[2]
            dict2['email'] = c[3]
            dict2['valor'] = donacion.valor
            dict2['fecha'] = donacion.fecha_donacion
            dict2['moneda'] = donacion.moneda
            dict.append(dict2)
        return Response(dict)
