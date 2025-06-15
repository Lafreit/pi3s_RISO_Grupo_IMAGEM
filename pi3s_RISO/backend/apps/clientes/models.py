# C:\pi3s\pi3s_RISO\backend\apps\clientes\models.py

from django.db import models
# Importar validadores customizados, se já os tiver
# from .validators import validate_cpf, validate_cnpj, validate_cep

class Cliente(models.Model):
    # ID 2.1: Nome Completo / Razão Social
    TIPO_CLIENTE_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]
    tipo_cliente = models.CharField(
        max_length=2,
        choices=TIPO_CLIENTE_CHOICES,
        default='PF', # Pode ser 'PF' ou 'PJ' como padrão
        verbose_name="Tipo de Cliente"
    )
    nome_completo_razao_social = models.CharField( # ID 2.1.1
        max_length=255,
        verbose_name="Nome Completo / Razão Social",
        help_text="Nome completo para pessoa física ou Razão Social para pessoa jurídica."
    )
    # ID 2.1.3: Validação de mínimo de caracteres pode ser feita no serializer ou em um validador customizado.

    # ID 2.3: CPF para PF, CNPJ para PJ
    cpf = models.CharField( # ID 2.3.1
        max_length=11,
        unique=True,
        blank=True,
        null=True,
        verbose_name="CPF",
        # Adicionar validador de CPF aqui quando tiver: validators=[validate_cpf]
    )
    cnpj = models.CharField( # ID 2.3.1
        max_length=14,
        unique=True,
        blank=True,
        null=True,
        verbose_name="CNPJ",
        # Adicionar validador de CNPJ aqui quando tiver: validators=[validate_cnpj]
    )
    # ID 2.3.4: A validação 'unique=True' já garante que não haverá duplicidade.

    # ID 2.2: Endereço
    cep = models.CharField( # ID 2.2.1
        max_length=9, # Ex: "12345-678"
        blank=True,
        null=True,
        verbose_name="CEP",
        # Adicionar validador de formato de CEP aqui: validators=[validate_cep]
    )
    rua = models.CharField( # ID 2.2.1
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Rua"
    )
    numero = models.CharField( # ID 2.2.1 (Pode ser string para "S/N" ou números grandes)
        max_length=10,
        verbose_name="Número" # ID 2.2.1: Obrigatório
    )
    complemento = models.CharField( # ID 2.2.1
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Complemento"
    )
    bairro = models.CharField( # ID 2.2.1
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Bairro"
    )
    cidade = models.CharField( # ID 2.2.1
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Cidade"
    )
    # ID 2.2.1: Lista de seleção das Unidades Federativas do Brasil
    ESTADO_CHOICES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
    ]
    estado = models.CharField( # ID 2.2.1
        max_length=2,
        choices=ESTADO_CHOICES,
        blank=True,
        null=True,
        verbose_name="Estado"
    )

    # ID 2.4: Meios de Contato
    telefone_principal = models.CharField( # ID 2.4.1
        max_length=20, # Ex: "(99) 99999-9999"
        verbose_name="Telefone Principal"
        # ID 2.4.2: Adicionar validador de formato de telefone aqui
    )
    telefone_secundario = models.CharField( # ID 2.4.1
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Telefone Secundário"
        # ID 2.4.3: Adicionar validador de formato de telefone aqui
    )
    email = models.EmailField( # ID 2.4.1
        max_length=255,
        blank=True,
        null=True,
        verbose_name="E-mail",
        # ID 2.4.4: A validação de formato é feita pelo EmailField, mas mais complexas podem ir para um validador
    )

    # Campos de controle/auditoria e status
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    ultima_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    ativo = models.BooleanField(default=True, verbose_name="Ativo") # Campo para ativar/desativar cliente

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome_completo_razao_social'] # Ordem pela Razão Social/Nome Completo

    def __str__(self):
        return self.nome_completo_razao_social

    def clean(self):
        # Validação personalizada para CPF/CNPJ
        if self.tipo_cliente == 'PF' and not self.cpf:
            from django.core.exceptions import ValidationError
            raise ValidationError({'cpf': 'CPF é obrigatório para Pessoa Física.'})
        if self.tipo_cliente == 'PJ' and not self.cnpj:
            from django.core.exceptions import ValidationError
            raise ValidationError({'cnpj': 'CNPJ é obrigatório para Pessoa Jurídica.'})

        if self.tipo_cliente == 'PF' and self.cnpj:
            from django.core.exceptions import ValidationError
            raise ValidationError({'cnpj': 'Não é permitido CNPJ para Pessoa Física.'})
        if self.tipo_cliente == 'PJ' and self.cpf:
            from django.core.exceptions import ValidationError
            raise ValidationError({'cpf': 'Não é permitido CPF para Pessoa Jurídica.'})

        # Limpa CPF/CNPJ se o tipo de cliente for alterado
        if self.tipo_cliente == 'PF':
            self.cnpj = None
        elif self.tipo_cliente == 'PJ':
            self.cpf = None

        super().clean()

    # Métodos para integração com serviço de CEP (ID 2.2.2)
    # Isso seria implementado no Serializer ou View, ou como um método de classe/instância aqui
    # Exemplo (apenas ilustrativo, não funcional sem uma API externa):
    # def preencher_endereco_por_cep(self):
    #     if self.cep:
    #         # Lógica para chamar API de CEP (ex: ViaCEP)
    #         # e preencher self.rua, self.bairro, self.cidade, self.estado
    #         pass