# apps/veiculos/views.py
from rest_framework import viewsets, permissions # Adicione 'permissions' aqui
from .models import Veiculo
from .serializers import VeiculoSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all().order_by('placa') # Ajuste se o campo for diferente
    serializer_class = VeiculoSerializer
    permission_classes = [permissions.IsAuthenticated] # <-- Adicione esta linha