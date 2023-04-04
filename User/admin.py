from django.contrib import admin
from User.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from User.forms import CustomUserCreationForm

# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    # add_form = CustomUserCreationForm

    ordering = ['last_name']

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'email',
                    'first_name',
                    'last_name',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_active',
                    'is_superuser'
                ),
            },
        ),
    )
