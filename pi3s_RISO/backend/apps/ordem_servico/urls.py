# apps/ordem_servico/urls.py
from rest_framework.routers import DefaultRouter
from .views import OrdemServicoViewSet, ItemOrdemServicoViewSet

router = DefaultRouter()
# Registra os ViewSets com prefixos vazios.
# Os prefixos 'ordem-servico/' e 'itens-ordem-servico/' virão do novo_projeto/urls.py
router.register(r'ordem-servico', OrdemServicoViewSet, basename='ordem_servico')
router.register(r'itens-ordem-servico', ItemOrdemServicoViewSet, basename='item_ordem_servico')


app_name = 'ordem_servico' # Define o namespace para este app

urlpatterns = router.urls # Apenas as URLs geradas pelo router