# apps/clientes/views.py
from rest_framework import viewsets, permissions
# Importe seu modelo de Cliente
from .models import Cliente
# Importe seu serializer de ClienteSerializer
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nome_completo')
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]  # Permissão: Apenas usuários autenticados podem acessar os endpoints de Cliente