# apps/departamentos/urls.py

from rest_framework.routers import DefaultRouter
# Assumindo que você tem um DepartamentoViewSet definido em apps/departamentos/views.py
from .views import DepartamentoViewSet

router = DefaultRouter()
# Registra o DepartamentoViewSet com prefixo vazio.
# O prefixo 'departamentos/' virá do novo_projeto/urls.py
router.register(r'', DepartamentoViewSet, basename='departamento')

app_name = 'departamentos' # Define o namespace para este app

urlpatterns = router.urls # Apenas as URLs geradas pelo router