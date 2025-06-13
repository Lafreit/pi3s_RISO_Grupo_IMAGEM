# apps/autenticacao/models.py
from django.db import models # <-- Adicione esta linha!
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    tentativas_falhas = models.IntegerField(default=0)
    # ... seus outros campos e métodos