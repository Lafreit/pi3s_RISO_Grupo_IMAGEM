# apps/autenticacao/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # Importe UserAdmin
from .models import Usuario # Importe seu modelo customizado Usuario

# Opcional: Você pode criar uma classe de Admin para personalizar a exibição
# Mas para começar, vamos usar a UserAdmin padrão para o seu modelo.
# class UsuarioAdmin(UserAdmin):
#    pass

# Registrar o seu modelo Usuario com o admin
admin.site.register(Usuario, UserAdmin) # Registre Usuario usando UserAdmin