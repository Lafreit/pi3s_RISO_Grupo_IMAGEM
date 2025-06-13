# apps/empregados/views.py
from rest_framework import viewsets, permissions
from .models import Empregado
from .serializers import EmpregadoSerializer

class EmpregadoViewSet(viewsets.ModelViewSet):
    queryset = Empregado.objects.all().order_by('nome_completo')
    serializer_class = EmpregadoSerializer
    permission_classes = [permissions.IsAuthenticated]