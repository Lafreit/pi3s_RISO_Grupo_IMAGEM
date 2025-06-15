# apps/veiculos/models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils import timezone # Para validação de ano

# Validador de Placa Mercosul ou Antiga
placa_validator = RegexValidator(
    regex=r'^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$|^[A-Z]{3}[0-9]{4}$',
    message='A placa deve estar no formato Mercosul (LLLNXNN) ou anterior (LLLNNNN).',
    code='invalid_plate'
)

class Veiculo(models.Model):
    TIPO_VEICULO_CHOICES = [
        ('AUTOMOVEL', 'Automóvel'),
        ('MOTOCICLETA', 'Motocicleta'),
    ]

    tipo = models.CharField(
        max_length=15,
        choices=TIPO_VEICULO_CHOICES,
        verbose_name="Tipo do Veículo"
    )

    placa = models.CharField(
        max_length=10,
        unique=True,
        validators=[placa_validator],
        verbose_name="Placa"
    )

    marca = models.CharField(max_length=100, verbose_name="Marca")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")

    ano_fabricacao = models.IntegerField(
        validators=[
            MinValueValidator(1900, message="O ano de fabricação não pode ser anterior a 1900."),
            MaxValueValidator(timezone.now().year + 1, message="O ano de fabricação não pode ser futuro.")
        ],
        verbose_name="Ano de Fabricação"
    )

    quilometragem_atual = models.PositiveIntegerField(
        verbose_name="Quilometragem Atual",
        validators=[MinValueValidator(0, message="A quilometragem não pode ser negativa.")]
    )

    cor = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Cor"
    )

    observacoes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Outras Informações"
    )

    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        ordering = ['placa']

    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo} ({self.ano_fabricacao})"