from django.urls import path
from Persona.api.views import *

urlpatterns = [
    path('registrar_voluntario/', RegisterVoluntarioView.as_view()),
    path('ver_niños/', NiñoView.as_view()),
    path('ver_voluntarios', VoluntarioView.as_view()),
]
