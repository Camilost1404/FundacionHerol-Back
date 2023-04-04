from django import forms
from django.contrib.auth.forms import UserCreationForm
from User.models import User


class CustomUserCreationForm(UserCreationForm):
    # Agregar campos adicionales o personalizar la creación del usuario si es necesario

    username = forms.CharField(label='Usuario')
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido')
    direccion = forms.CharField(label='Dirección')
    email = forms.EmailField(label='Correo')
    password1 = forms.CharField(
        label='Contraseña:', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar Contraseña:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'is_staff',
            'is_active',
            'is_superuser'
        ]

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
