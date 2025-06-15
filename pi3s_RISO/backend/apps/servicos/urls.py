# C:\pi3s\pi3s_RISO\backend\apps\servicos\urls.py

from rest_framework.routers import DefaultRouter
from .views import ServicoViewSet # Note o '.' para importação relativa

router = DefaultRouter()
router.register(r'servicos', ServicoViewSet) # Será /api/servicos/

urlpatterns = router.urls