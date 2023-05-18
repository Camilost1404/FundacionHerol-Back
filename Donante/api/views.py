from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSession(APIView):
    def post(self, request):
        # Obtener los datos del precio y el cliente desde el frontend
        price_id = request.data.get('price_id')
        customer_email = request.data.get('customer_email')

        try:
            # Crear una sesión de Checkout de Stripe
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': price_id,
                    'quantity': 1,
                }],
                mode='payment',
                success_url='https://example.com',
                cancel_url='https://example.com',
                customer_email=customer_email,  # Pasar el correo electrónico del cliente
            )

            # Devolver la información de la sesión de Stripe al frontend
            return Response({'id': session.url})

        except Exception as e:
            # Devolver un mensaje de error si no se pudo crear la sesión de Stripe
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
