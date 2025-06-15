# apps/departamentos/apps.py
from django.apps import AppConfig

class DepartamentosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.departamentos' # <-- ESSA LINHA É CRÍTICA!
    verbose_name = 'Departamentos'