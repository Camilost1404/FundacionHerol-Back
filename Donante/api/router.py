from django.urls import path
from Donante.api.views import *


urlpatterns = [
    path('donante/create-checkout-session/' , CreateCheckoutSession.as_view()),
]