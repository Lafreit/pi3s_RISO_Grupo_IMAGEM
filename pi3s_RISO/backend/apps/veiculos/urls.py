# apps/veiculos/urls.py

from rest_framework.routers import DefaultRouter
# Assumindo que você tem um VeiculoViewSet definido em apps/veiculos/views.py
from .views import VeiculoViewSet

router = DefaultRouter()
# Registra o VeiculoViewSet com prefixo vazio.
# O prefixo 'veiculos/' virá do novo_projeto/urls.py
router.register(r'', VeiculoViewSet, basename='veiculo')

app_name = 'veiculos' # Define o namespace para este app

urlpatterns = router.urls # Apenas as URLs geradas pelo router