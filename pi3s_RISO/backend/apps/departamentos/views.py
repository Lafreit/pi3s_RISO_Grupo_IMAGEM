# apps/departamentos/views.py
from rest_framework import viewsets, permissions
from .models import Departamento
from .serializers import DepartamentoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all().order_by('nome')
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]