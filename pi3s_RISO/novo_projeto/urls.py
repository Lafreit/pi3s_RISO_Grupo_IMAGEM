# novo_projeto/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Adicione estas 3 linhas para o drf-spectacular (devem estar no topo)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# --- Importações dos Routers dos Apps (DRF) ---
# Importe os routers de cada um dos seus apps que usam DefaultRouter.
# Certifique-se de que cada apps/<nome_do_app>/urls.py define 'router' e 'app_name'.
from apps.clientes.urls import router as clientes_router
from apps.departamentos.urls import router as departamentos_router
from apps.empregados.urls import router as empregados_router
from apps.ordem_servico.urls import router as ordem_servico_router # <-- NOVO: Router da Ordem de Serviço
from apps.servicos.urls import router as servicos_router
from apps.veiculos.urls import router as veiculos_router

# --- Importação de URLs de Apps que NÃO usam DefaultRouter ou têm URLs customizadas ---
# O app 'autenticacao' geralmente tem URLs mais customizadas, então o incluímos diretamente.
# Se o seu apps/autenticacao/urls.py TAMBÉM usar um DefaultRouter, ajuste como os outros.
# path("api/autenticacao/", include("apps.autenticacao.urls")),

def home(request):
    """View simples para a página inicial."""
    return HttpResponse("<h1>Bem-vindo ao Projeto Django!</h1>")

urlpatterns = [
    # URLs do Django Admin
    path("admin/", admin.site.urls),

    # Página inicial do projeto (não faz parte da API REST)
    path("", home),

    # --- API Endpoints ---
    # Todos os endpoints da API RESTful serão prefixados com 'api/'.
    # O 'include' dos routers (que internamente têm prefixo r'') garante URLs limpas
    # como /api/clientes/, /api/servicos/, /api/empregados/, etc.

    # Autenticação (assumindo que apps.autenticacao.urls não usa DefaultRouter em sua raiz)
    path("api/autenticacao/", include("apps.autenticacao.urls")),

    # Inclua os routers dos seus apps
    path('api/clientes/', include(clientes_router.urls)),
    path('api/departamentos/', include(departamentos_router.urls)),
    path('api/empregados/', include(empregados_router.urls)),
    path('api/ordem-servico/', include(ordem_servico_router.urls)), # <-- NOVO: URL para Ordem de Serviço
    path('api/servicos/', include(servicos_router.urls)),
    path('api/veiculos/', include(veiculos_router.urls)),

    # --- Documentação da API (DRF-Spectacular) ---
    # Configuração para a documentação interativa da API (Swagger UI / ReDoc)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]