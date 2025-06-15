# apps/servicos/admin.py
from django.contrib import admin
from .models import Servico

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_servico',
        'get_tipo_servico_display', # Exibe o label do choice field
        'valor_unitario',
        'tempo_medio_execucao',
        'unidade_tempo',
        'quantidade_rodas',
        'prazo_entrega_dias',
        'data_criacao'
    )
    list_filter = (
        'tipo_servico',
        'unidade_tempo',
        'data_criacao'
    )
    search_fields = (
        'codigo_servico',
        'descricao_detalhada',
        'tipo_servico_outro'
    )
    # Define a ordem dos campos no formulário de adição/edição
    fieldsets = (
        (None, {
            'fields': ('codigo_servico', 'tipo_servico', 'tipo_servico_outro', 'descricao_detalhada')
        }),
        ('Detalhes do Preço e Tempo', {
            'fields': ('valor_unitario', 'tempo_medio_execucao', 'unidade_tempo')
        }),
        ('Detalhes Adicionais', {
            'fields': ('quantidade_rodas', 'prazo_entrega_dias'),
            'classes': ('collapse',) # Opcional: para recolher esta seção por padrão
        }),
    )
    readonly_fields = ('data_criacao', 'data_atualizacao')