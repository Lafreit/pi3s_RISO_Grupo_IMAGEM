# apps/servicos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServicoViewSet

# Crie um router e registre nossos viewsets com ele.
# ATENÇÃO: O prefixo aqui é VAZIO '' para que o router gere URLs como '/' e '/{pk}/'
# O prefixo 'servicos/' virá do novo_projeto/urls.py
router = DefaultRouter()
router.register(r'', ServicoViewSet, basename='servico') # <-- PREFIXO VAZIO AQUI!

app_name = 'servicos' # Importante para namespacing

# As URLs da API são determinadas automaticamente pelo router.
# Não há necessidade de 'path('api/', include(router.urls))' aqui.
# Apenas exporte o router.urls
urlpatterns = router.urls # <-- APENAS router.urls AQUI