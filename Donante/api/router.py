from django.urls import path
from Donante.api.views import *


urlpatterns = [
    path('donacion', RealizarDonacion.as_view()),
    path('donante/registrar', DonanteRegister.as_view()),
    path('ver_donacion/', VerDonacion.as_view()),
]