from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import SignInSerializer, SignUpSerializer



class SignUp(viewsets.ModelViewSet):
    serializer_class = SignUpSerializer

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "Сообщение": "Пользователь успегн зарегестрирован!",
                "data": {"username": serializer.data.get("username"),
                         "email": serializer.data.get("email"),
                         },
            }
            return Response(data=response)
        return Response(data=serializer.errors)



class SignIn(APIView):
    serializer_class = SignInSerializer
    """API endpoint for signing in and checking the status of a user's session."""
    def post(self, request: Request):
        """
        "post" for signing in a user using their email and password
        """
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken().for_user(user)
            response = {
                "Сообщение": "Вы успешно вошли в систему!",
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                },
                "user": user.username}
            return Response(data=response)
        else:
            return Response(data={"Сообщение": "Вы не аторизованы! \nЗарегестрируйтесь!"})
