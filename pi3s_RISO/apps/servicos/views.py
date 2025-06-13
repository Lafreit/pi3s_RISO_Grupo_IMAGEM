# apps/servicos/views.py
from rest_framework import viewsets, permissions
from .models import Servico
from .serializers import ServicoSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all().order_by('descricao_detalhada')
    serializer_class = ServicoSerializer
    permission_classes = [permissions.IsAuthenticated]