# apps/clientes/urls.py

from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet

router = DefaultRouter()
# Registra o ClienteViewSet com prefixo vazio.
# O prefixo 'clientes/' virá do novo_projeto/urls.py
router.register(r'clientes', ClienteViewSet, basename='clientes')  # Será acessível em /api/clientes/

app_name = 'clientes' # Define o namespace para este app

urlpatterns = [] + router.urls # O router.urls já inclui as URLs necessárias, então não precisamos adicionar mais nada aqui.