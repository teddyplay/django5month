from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def create(self, validated_data):
        password =  validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class SignInSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["password", "email"]

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        return serializers.ValidationError("Такого пользователя нет в базе!")



