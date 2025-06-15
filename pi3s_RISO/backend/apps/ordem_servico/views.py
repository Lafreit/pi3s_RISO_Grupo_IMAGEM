# apps/ordem_servico/views.py
from rest_framework import viewsets, permissions # Adicione 'permissions' aqui
from .models import OrdemServico, ItemOrdemServico
from .serializers import OrdemServicoSerializer, ItemOrdemServicoSerializer

class OrdemServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemServico.objects.all().order_by('-data_emissao')
    serializer_class = OrdemServicoSerializer
    permission_classes = [permissions.IsAuthenticated] # <-- Adicione esta linha

class ItemOrdemServicoViewSet(viewsets.ModelViewSet):
    queryset = ItemOrdemServico.objects.all()
    serializer_class = ItemOrdemServicoSerializer
    permission_classes = [permissions.IsAuthenticated] # <-- Adicione esta linha