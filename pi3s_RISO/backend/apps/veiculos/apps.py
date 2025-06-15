# C:\pi3s\pi3s_RISO\apps\veiculos\apps.py
from django.apps import AppConfig

class VeiculosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.veiculos' # <-- ESSA LINHA É CRÍTICA!
    verbose_name = 'Veículos' # Nome amigável para o admin do Django