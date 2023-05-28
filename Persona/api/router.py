from django.urls import path
from Persona.api.views import *

urlpatterns = [
    path('registrar_voluntario/', RegisterVoluntarioView.as_view()),
    path('ver_niños/', NiñoView.as_view()),
    path('ver_voluntarios', VoluntarioView.as_view()),
    path('guardar_niño/', GuardarNiño.as_view()),
    path('eliminar_niño/', BorrarNiño.as_view()),
    path('modificar_niño/', modificarNiño.as_view()),
    path('niño_esp/', NiñoEspecificoView.as_view()),
    path('voluntario_esp/', VoluntarioEspecifico.as_view()),
    path('eliminar_voluntario/', BorrarVoluntario.as_view()),
    path('estado_voluntario/', EstadoVoluntario.as_view()),
    path('modificar_voluntario/', ModificarVoluntario.as_view()),
]
