from django.urls import path

from User.api.views import *

urlpatterns = [
    path('users', ViewUser.as_view()),
    path('eliminar_user/', DeleteUser.as_view()),
    path('crear_user/', UserCreate.as_view()),
    path('user_esp', UserEspecifico.as_view()),
    path('modificar_user', ModificarUser.as_view()),
    path('super_update', UserSuperEstado.as_view()),
    path('active_update', UserActiveEstado.as_view()),
]