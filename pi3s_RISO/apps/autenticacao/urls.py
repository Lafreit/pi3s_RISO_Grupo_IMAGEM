# apps/autenticacao/urls.py

from django.urls import path
from .views import CustomTokenObtainPairView, UserRegisterView, UserListView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from django.views.generic import RedirectView

urlpatterns = [
    # Redirecionamento para login
    path('', RedirectView.as_view(url='login/', permanent=False), name='login_redirect'),

    # API de Login e Tokens (para requisições POST)
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obter'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # API de Registro de Usuários (para requisições POST)
    path('register/', UserRegisterView.as_view(), name='api_register'),

    # API para listar usuários
    path('users/', UserListView.as_view(), name='user-list'),

    # Views de frontend que renderizam templates (aqui as views são chamadas sem template_name no as_view)
    path('login/', CustomTokenObtainPairView.as_view(), name='login'), # <-- ALTERADO AQUI!
    path('logout/', RedirectView.as_view(url='/autenticacao/login/', permanent=False), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'), # <-- ALTERADO AQUI!
]