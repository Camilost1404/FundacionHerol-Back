from django.urls import path
from Persona.api.views import *

urlpatterns = [
    path('registrar_voluntario/', RegisterVoluntarioView.as_view()),
]
