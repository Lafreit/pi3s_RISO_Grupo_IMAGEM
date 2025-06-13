from django.db import models
# IMPORTANTE: Copie também estas linhas de importação, se estiverem lá!
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator

class Cliente(models.Model):
    TIPO_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    nome_completo = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(3)],
        verbose_name="Nome Completo/Razão Social"
    )
    tipo = models.CharField(
        max_length=2,
        choices=TIPO_CHOICES,
        default='PF',
        verbose_name="Tipo de Cliente"
    )
    cpf = models.CharField(
        max_length=14,
        blank=True,
        null=True,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
                message='Formato de CPF inválido. Use: 000.000.000-00',
            )
        ],
        verbose_name="CPF"
    )
    cnpj = models.CharField(
        max_length=18,
        blank=True,
        null=True,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$',
                message='Formato de CNPJ inválido. Use: 00.000.000/0000-00',
            )
        ],
        verbose_name="CNPJ"
    )
    cep = models.CharField(
        max_length=9,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\d{5}-\d{3}$',
                message='Formato de CEP inválido. Use: 00000-000',
            )
        ],
        verbose_name="CEP"
    )
    rua = models.CharField(max_length=255, blank=True, null=True, verbose_name="Rua")
    numero = models.CharField(max_length=10, verbose_name="Número")
    complemento = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Complemento"
    )
    bairro = models.CharField(max_length=100, blank=True, null=True, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade")
    estado = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        choices=[
            ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
            ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
            ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
        ],
        verbose_name="Estado"
    )
    telefone_principal = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\(\d{2}\) \d{4,5}-\d{4}$',
                message='Formato de telefone principal inválido. Use: (00) 0000-0000 ou (00) 00000-0000',
            )
        ],
        verbose_name="Telefone Principal"
    )
    telefone_secundario = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\(\d{2}\) \d{4,5}-\d{4}$',
                message='Formato de telefone secundário inválido. Use: (00) 0000-0000 ou (00) 00000-0000',
            )
        ],
        verbose_name="Telefone Secundário"
    )
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome_completo']

    def __str__(self):
        return self.nome_completo
# Create your models here.
