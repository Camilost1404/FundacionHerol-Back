from django.urls import path

from User.api.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users', ViewUser.as_view()),
    path('eliminar_user/', DeleteUser.as_view()),
    path('crear_user/', UserCreate.as_view()),
    path('user_esp', UserEspecifico.as_view()),
    path('modificar_user', ModificarUser.as_view()),
    path('super_update', UserSuperEstado.as_view()),
    path('active_update', UserActiveEstado.as_view()),
    path('contact', EmailContacto.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/auth', UserAuth.as_view()),
    path('user/logout', LogoutView.as_view()),
]
