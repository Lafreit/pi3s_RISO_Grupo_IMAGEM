# apps/autenticacao/views.py
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .serializers import CustomTokenObtainPairSerializer, UserRegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    template_name = 'autenticacao/login.html' # <-- ADICIONADO AQUI!

    def get(self, request, *args, **kwargs):
        # Esta é a parte que renderiza o template para a requisição GET na URL de login
        return render(request, self.template_name)

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer
    template_name = 'autenticacao/register.html' # <-- ADICIONADO AQUI!

    def get(self, request, *args, **kwargs):
        # Adicione este método GET para que a view possa renderizar o template para a página de registro
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Opcional: Logar o usuário após o registro e retornar tokens (removido para evitar confusão com o redirect)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]