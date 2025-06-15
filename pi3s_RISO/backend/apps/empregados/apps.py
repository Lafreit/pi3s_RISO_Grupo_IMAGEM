# apps/empregados/apps.py
from django.apps import AppConfig

class EmpregadosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.empregados'
    verbose_name = 'Empregados'