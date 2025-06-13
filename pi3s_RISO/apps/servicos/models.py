# apps/servicos/models.py
from django.db import models
from django.core.validators import MinValueValidator

class Servico(models.Model):
    # ID 4.1.1 e 4.1.2: Código do Serviço Único e Obrigatório
    codigo_servico = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Código do Serviço",
        help_text="Código único para identificar o serviço."
    )

    # ID 4.2.1: Tipo do Serviço Obrigatório
    TIPO_SERVICO_CHOICES = [
        ('B', 'Balanceamento'),
        ('A', 'Alinhamento'),
        ('R', 'Reforma de Rodas'),
        ('O', 'Outro') # Adicione esta opção se quiser um texto livre para "Outro"
    ]
    tipo_servico = models.CharField(
        max_length=1, # Ajuste o max_length se os códigos forem maiores (ex: 'BALANCEAMENTO')
        choices=TIPO_SERVICO_CHOICES,
        verbose_name="Tipo do Serviço"
    )
    # Se 'Outro' for selecionado e você quiser um campo de texto livre adicional
    tipo_servico_outro = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Especifique o Tipo do Serviço (se 'Outro')"
    )


    # ID 4.3.1: Descrição Detalhada (Opcional)
    descricao_detalhada = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição Detalhada do Serviço",
        help_text="Informações adicionais sobre o serviço."
    )

    # ID 4.4.1 e 4.4.2: Valor Unitário Obrigatório e Positivo
    valor_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01, message="O valor unitário deve ser um número positivo.")],
        verbose_name="Valor Unitário"
    )

    # ID 4.5.1, 4.5.2 e 4.5.3: Tempo Médio de Execução e Unidade de Tempo
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
        default='M', # Padrão para minutos
        verbose_name="Unidade de Tempo"
    )

    # ID 4.6.1 e 4.6.2: Quantidade Padrão de Rodas (Opcional e Positivo)
    quantidade_rodas = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1, message="A quantidade de rodas deve ser um número inteiro positivo.")],
        verbose_name="Quantidade Padrão de Rodas",
        help_text="Número de rodas envolvidas no serviço (opcional)."
    )

    # ID 4.7.1 e 4.7.2: Prazo de Entrega Padrão (Opcional e Positivo)
    prazo_entrega_dias = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1, message="O prazo de entrega deve ser um número inteiro positivo.")],
        verbose_name="Prazo de Entrega Padrão (dias)",
        help_text="Prazo em dias para a conclusão do serviço (opcional)."
    )

    # Campos de controle/auditoria (já tínhamos algo similar)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ['codigo_servico'] # Ordem padrão pelo código do serviço

    def __str__(self):
        return f"{self.codigo_servico} - {self.get_tipo_servico_display()}"