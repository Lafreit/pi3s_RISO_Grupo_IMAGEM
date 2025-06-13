# apps/empregados/urls.py

from rest_framework.routers import DefaultRouter
from .views import EmpregadoViewSet

router = DefaultRouter()
# Registra o EmpregadoViewSet com prefixo vazio.
# O prefixo 'empregados/' virá do novo_projeto/urls.py
router.register(r'', EmpregadoViewSet, basename='empregado')
app_name = 'empregados' # Define o namespace para este app

urlpatterns = router.urls # Apenas as URLs geradas pelo router