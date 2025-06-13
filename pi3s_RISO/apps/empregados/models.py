# apps/empregados/models.py
from django.db import models
from apps.departamentos.models import Departamento # Importa o modelo Departamento

class Empregado(models.Model):
    # ID 10.2.1: Código único para cada empregado (gerado automaticamente)
    codigo_empregado = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Código do Empregado",
        help_text="Código único gerado automaticamente para o empregado."
    )

    nome_completo = models.CharField(max_length=255, verbose_name="Nome Completo")

    # ID 10.1.1: Seleção do departamento ao qual o empregado pertence
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.SET_NULL, # Mantém empregado se departamento for deletado (pode ser CASCADE)
        null=True,
        blank=True, # Permitir que um empregado não tenha departamento vinculado inicialmente
        related_name='empregados',
        verbose_name="Departamento"
    )

    # ID 10.3.1: Código de dependentes (opcional)
    codigo_dependentes = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Código de Dependentes",
        help_text="Código para identificação de dependentes do empregado (opcional)."
    )

    # ID 10.4.1: Cargo do empregado (lista predefinida)
    CARGO_CHOICES = [
        ('Gerente', 'Gerente'),
        ('Supervisor', 'Supervisor'),
        ('Mecânico', 'Mecânico'),
        ('Vendedor', 'Vendedor'),
        ('Atendente', 'Atendente'),
        ('Administrativo', 'Administrativo'),
        ('Outro', 'Outro'),
    ]
    cargo = models.CharField(
        max_length=50,
        choices=CARGO_CHOICES,
        default='Outro',
        verbose_name="Cargo"
    )

    # ID 10.5.1: Nacionalidade
    nacionalidade = models.CharField(max_length=100, verbose_name="Nacionalidade")

    # ID 10.6.1: Naturalidade (cidade de nascimento)
    naturalidade = models.CharField(max_length=100, verbose_name="Naturalidade")

    # ID 10.7.1: Cidade e UF de residência
    cidade_residencia = models.CharField(max_length=100, verbose_name="Cidade de Residência")
    UF_CHOICES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'),
        ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'),
        ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
        ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'),
        ('SE', 'Sergipe'), ('TO', 'Tocantins'),
    ]
    uf_residencia = models.CharField(
        max_length=2,
        choices=UF_CHOICES,
        verbose_name="UF de Residência"
    )

    # ID 10.8.1: Data de nascimento
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")

    # ID 10.9.1: Estado civil
    ESTADO_CIVIL_CHOICES = [
        ('Solteiro', 'Solteiro'),
        ('Casado', 'Casado'),
        ('Divorciado', 'Divorciado'),
        ('Viúvo', 'Viúvo'),
        ('Separado', 'Separado'),
        ('União Estável', 'União Estável'),
    ]
    estado_civil = models.CharField(
        max_length=20,
        choices=ESTADO_CIVIL_CHOICES,
        default='Solteiro',
        verbose_name="Estado Civil"
    )

    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')

    class Meta:
        verbose_name = "Empregado"
        verbose_name_plural = "Empregados"
        ordering = ['nome_completo']

    def __str__(self):
        return self.nome_completo

    # Lógica para gerar o código do empregado (ID 10.2.1)
    def save(self, *args, **kwargs):
        if not self.codigo_empregado:
            # Obtém o último ID do banco de dados, ou 0 se não houver registros
            last_id = Empregado.objects.all().order_by('-id').first()
            new_id = (last_id.id if last_id else 0) + 1
            self.codigo_empregado = f"EMP{new_id:04d}" # Ex: EMP0001, EMP0002
        super().save(*args, **kwargs)