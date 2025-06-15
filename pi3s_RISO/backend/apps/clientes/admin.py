# C:\pi3s\pi3s_RISO\backend\apps\clientes\admin.py

from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Ajustar os campos para os novos nomes definidos em models.py
    list_display = ('nome_completo_razao_social', 'tipo_cliente', 'cpf', 'cnpj', 'telefone_principal', 'email', 'ativo', 'data_cadastro')
    search_fields = ('nome_completo_razao_social', 'cpf', 'cnpj', 'email', 'telefone_principal')
    list_filter = ('tipo_cliente', 'ativo', 'data_cadastro', 'estado') # Adicionei 'estado' e 'tipo_cliente'
    # Campos que só aparecerão na página de detalhes do cliente
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('tipo_cliente', 'nome_completo_razao_social', 'ativo')
        }),
        ('Documentos', {
            'fields': ('cpf', 'cnpj')
        }),
        ('Contato', {
            'fields': ('telefone_principal', 'telefone_secundario', 'email')
        }),
        ('Endereço', {
            'fields': ('cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado')
        }),
        ('Datas', {
            'fields': ('data_cadastro', 'ultima_atualizacao'),
            'classes': ('collapse',), # Opcional: faz a seção ser recolhível
        }),
    )
    # Exemplo de como controlar quais campos são editáveis no formulário
    readonly_fields = ('data_cadastro', 'ultima_atualizacao')