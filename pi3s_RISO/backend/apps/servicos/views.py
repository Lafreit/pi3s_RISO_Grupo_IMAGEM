# apps/servicos/views.py
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Servico
from .serializers import ServicoSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all().order_by('descricao_detalhada')
    serializer_class = ServicoSerializer
    permission_classes = [permissions.IsAuthenticated]

ServicoViewSet.permission_classes = [IsAuthenticated]  # Garante que apenas usuários autenticados possam acessar o ServicoViewSet