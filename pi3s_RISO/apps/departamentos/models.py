# apps/departamentos/models.py
from django.db import models

class Departamento(models.Model):
    # ID 9.1.1: Código único para cada departamento
    codigo_departamento = models.CharField(
        max_length=50,
        unique=True,
        null=True, # Permitir nulo para que possamos gerar automaticamente no save, se necessário
        blank=True,
        verbose_name="Código do Departamento",
        help_text="Código único para identificação do departamento."
    )
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Departamento")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['nome']

    def __str__(self):
        return self.nome

    # Lógica para gerar o código do departamento (ID 9.1.1 e 9.1.2)
    # Pode ser um contador simples ou algo mais sofisticado
    def save(self, *args, **kwargs):
        if not self.codigo_departamento:
            # Encontra o último ID e incrementa para gerar um código sequencial simples
            # Se preferir um formato como "DEP001", "DEP002", precisaria de um pouco mais de lógica
            last_id = Departamento.objects.all().order_by('-id').first()
            new_id = (last_id.id if last_id else 0) + 1
            self.codigo_departamento = f"DEP{new_id:03d}" # Ex: DEP001, DEP002
        super().save(*args, **kwargs)