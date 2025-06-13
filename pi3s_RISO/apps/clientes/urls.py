# apps/clientes/urls.py

from rest_framework.routers import DefaultRouter
# Assumindo que você tem um ClienteViewSet definido em apps/clientes/views.py
from .views import ClienteViewSet

router = DefaultRouter()
# Registra o ClienteViewSet com prefixo vazio.
# O prefixo 'clientes/' virá do novo_projeto/urls.py
router.register(r'', ClienteViewSet, basename='cliente')

app_name = 'clientes' # Define o namespace para este app

urlpatterns = router.urls # Apenas as URLs geradas pelo router