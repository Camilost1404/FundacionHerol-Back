from rest_framework import serializers

from User.models import *


class UserViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'password', 'username', 'is_superuser']

    def create(self, validated_data):
        usuario = User.objects.create_user(email=validated_data['email'],
                                           first_name=validated_data['first_name'],
                                           last_name=validated_data['last_name'],
                                           password=validated_data['password'],
                                           username=validated_data['username'],
                                           is_superuser=validated_data['is_superuser'])
        return usuario


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'is_active', 'is_superuser', 'is_staff']

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password')

        if password:
            instance.set_password(password)

        instance.save()
        return instance


class UserUpdateEstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['is_active']

    def update(self, instance, validated_data):
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        instance.save()
        return instance


class UserUpdateEstadoSerializer1(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['is_superuser']

    def update(self, instance, validated_data):
        instance.is_superuser = validated_data.get(
            'is_superuser', instance.is_superuser)
        instance.save()
        return instance
