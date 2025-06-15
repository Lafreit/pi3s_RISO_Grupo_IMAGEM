# C:\pi3s\pi3s_RISO\backend\apps\clientes\views.py

from rest_framework import viewsets
from rest_framework import permissions
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    
    queryset = Cliente.objects.all().order_by('nome_completo_razao_social')
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]