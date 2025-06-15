# pi3s_RISO/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Adicione estas 3 linhas para o drf-spectacular (devem estar no topo)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
# --- Importações dos Routers dos Apps (DRF) ---
# Importe os routers de cada um dos seus apps que usam DefaultRouter.
# Certifique-se de que cada apps/<nome_do_app>/urls.py define 'router'.
from apps.clientes.urls import router as clientes_router
from apps.departamentos.urls import router as departamentos_router
from apps.empregados.urls import router as empregados_router
from apps.ordem_servico.urls import router as ordem_servico_router
from apps.servicos.urls import router as servicos_router
from apps.veiculos.urls import router as veiculos_router

def home(request):
    """View simples para a página inicial."""
    return HttpResponse("<h1>Bem-vindo ao Projeto Django!</h1>")

urlpatterns = [
    # URLs do Django Admin
    path("admin/", admin.site.urls),

    # Página inicial do projeto (não faz parte da API REST)
    path("", home),

    # --- API Endpoints ---
    # Autenticação (assumindo que apps.autenticacao.urls não usa DefaultRouter em sua raiz)
    # Removida a duplicação daqui, mantendo apenas na lista urlpatterns abaixo.
    
    # Inclua os routers dos seus apps
    path('api/autenticacao/', include('apps.autenticacao.urls')), # ÚNICA ocorrência aqui
    path('api/clientes/', include(clientes_router.urls)),
    path('api/departamentos/', include(departamentos_router.urls)),
    path('api/empregados/', include(empregados_router.urls)),
    path('api/ordem-servico/', include(ordem_servico_router.urls)),
    path('api/servicos/', include(servicos_router.urls)),
    path('api/veiculos/', include(veiculos_router.urls)),

    # --- Documentação da API (DRF-Spectacular) ---
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]