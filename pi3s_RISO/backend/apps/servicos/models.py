# C:\pi3s\pi3s_RISO\backend\apps\servicos\models.py

from django.db import models
from django.core.validators import MinValueValidator # Se MinValueValidator for usado APENAS por Servico, mantenha.

class Servico(models.Model):
    # ... (Seu modelo Servico COMPLETO, como estava antes de eu pedir para adicionar Cliente) ...
    codigo_servico = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Código do Serviço",
        help_text="Código único para identificar o serviço."
    )

    TIPO_SERVICO_CHOICES = [
        ('B', 'Balanceamento'),
        ('A', 'Alinhamento'),
        ('R', 'Reforma de Rodas'),
        ('O', 'Outro')
    ]
    tipo_servico = models.CharField(
        max_length=1,
        choices=TIPO_SERVICO_CHOICES,
        verbose_name="Tipo do Serviço"
    )
    tipo_servico_outro = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Especifique o Tipo do Serviço (se 'Outro')"
    )

    descricao_detalhada = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição Detalhada do Serviço",
        help_text="Informações adicionais sobre o serviço."
    )

    valor_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01, message="O valor unitário deve ser um número positivo.")],
        verbose_name="Valor Unitário"
    )

    UNIDADE_TEMPO_CHOICES = [
        ('H', 'Horas'),
        ('M', 'Minutos'),
    ]
    tempo_medio_execucao = models.IntegerField(
        validators=[MinValueValidator(1, message="O tempo médio de execução deve ser um número inteiro positivo.")],
        verbose_name="Tempo Médio de Execução"
    )
    unidade_tempo = models.CharField(
        max_length=1,
        choices=UNIDADE_TEMPO_CHOICES,
        default='M',
        verbose_name="Unidade de Tempo"
    )

    quantidade_rodas = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1, message="A quantidade de rodas deve ser um número inteiro positivo.")],
        verbose_name="Quantidade Padrão de Rodas",
        help_text="Número de rodas envolvidas no serviço (opcional)."
    )

    prazo_entrega_dias = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1, message="O prazo de entrega deve ser um número inteiro positivo.")],
        verbose_name="Prazo de Entrega Padrão (dias)",
        help_text="Prazo em dias para a conclusão do serviço (opcional)."
    )

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ['codigo_servico']

    def __str__(self):
        return f"{self.codigo_servico} - {self.get_tipo_servico_display()}"