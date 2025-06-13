# apps/ordem_servico/models.py
from django.db import models
from django.utils import timezone # Para usar timezone.now()

# Importa os modelos necessários dos outros apps
from apps.clientes.models import Cliente # Modelo Cliente
from apps.veiculos.models import Veiculo   #Modelo Veiculo
from apps.empregados.models import Empregado # Modelo de Empregado

from apps.servicos.models import Servico # Servico é o tipo de serviço (e.g., Troca de Oleo)

class OrdemServico(models.Model):
    # ID 11.2.1: Código da Ordem de Serviço (gerado automaticamente)
    codigo_os = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Código da O.S.",
        help_text="Código único gerado automaticamente para a Ordem de Serviço."
    )

    # ID 11.1.1: Cliente (relação com o módulo Clientes)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT, # Protege para não apagar OS se cliente for deletado
        related_name='ordens_servico',
        verbose_name="Cliente"
    )

    # ID 11.1.2: Veículo (relação com o módulo Veículos)
    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.PROTECT, # Protege para não apagar OS se veículo for deletado
        related_name='ordens_servico',
        verbose_name="Veículo"
    )

    # ID 11.3.1: Data e Hora da Emissão da O.S. (automático)
    data_emissao = models.DateTimeField(auto_now_add=True, verbose_name="Data/Hora Emissão")

    # ID 11.4.1: Status da O.S. (lista predefinida)
    STATUS_CHOICES = [
        ('Aberta', 'Aberta'),
        ('Em Andamento', 'Em Andamento'),
        ('Aguardando Peças', 'Aguardando Peças'),
        ('Concluída', 'Concluída'),
        ('Cancelada', 'Cancelada'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Aberta',
        verbose_name="Status da O.S."
    )

    # ID 11.5.1: Empregado Responsável (relação com o módulo Empregados)
    empregado_responsavel = models.ForeignKey(
        Empregado,
        on_delete=models.SET_NULL, # Empregado pode ser nulo se for demitido
        null=True,
        blank=True,
        related_name='ordens_servico_responsavel',
        verbose_name="Empregado Responsável"
    )

    # ID 11.6.1: Observações Gerais
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações Gerais")

    # ID 11.7.1: Valor Total da O.S. (calculado, ou pode ser manual)
    # Pode ser calculado a partir dos itens da O.S. ou definido manualmente
    valor_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Valor Total da O.S."
    )

    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"
        ordering = ['-data_emissao'] # Ordena pela data de emissão mais recente

    def __str__(self):
        return f"OS {self.codigo_os} - Cliente: {self.cliente.nome_completo}"

    def save(self, *args, **kwargs):
        if not self.codigo_os:
            # Gerar um código único para a OS
            today_str = timezone.now().strftime('%Y%m%d') # AnoMesDia
            # Procura a última OS do dia para gerar um número sequencial
            last_os = OrdemServico.objects.filter(codigo_os__startswith=f'OS-{today_str}-').order_by('-codigo_os').first()
            if last_os:
                last_seq = int(last_os.codigo_os.split('-')[-1])
                new_seq = last_seq + 1
            else:
                new_seq = 1
            self.codigo_os = f"OS-{today_str}-{new_seq:04d}" # Ex: OS-20250612-0001
        super().save(*args, **kwargs)


class ItemOrdemServico(models.Model):
    # ID 11.8.1: Relação com a Ordem de Serviço pai
    ordem_servico = models.ForeignKey(
        OrdemServico,
        on_delete=models.CASCADE, # Se a OS for deletada, seus itens também são
        related_name='itens',
        verbose_name="Ordem de Serviço"
    )

    # ID 11.8.2: Tipo de Serviço (relação com o módulo Serviços, ou campo de texto)
    
    servico = models.ForeignKey(
        Servico, # Modelo Servico importado do app 'servicos'
        on_delete=models.PROTECT,
        related_name='itens_ordem_servico',
        verbose_name="Tipo de Serviço"
    )

    # ID 11.8.3: Descrição Detalhada do Serviço (texto livre)
    descricao_detalhada = models.TextField(verbose_name="Descrição Detalhada do Item")

    # ID 11.8.4: Quantidade
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, default=1.00, verbose_name="Quantidade")

    # ID 11.8.5: Valor Unitário
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Unitário")

    # ID 11.8.6: Valor Total do Item (calculado ou pode ser manual)
    valor_total_item = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Valor Total do Item"
    )

    class Meta:
        verbose_name = "Item da Ordem de Serviço"
        verbose_name_plural = "Itens da Ordem de Serviço"
        # Ajuda a garantir que um item específico de serviço não seja duplicado para a mesma OS.
        # Pode ser mais complexo dependendo da sua regra de negócio.
        unique_together = ('ordem_servico', 'servico', 'descricao_detalhada')

    def __str__(self):
        return f"OS {self.ordem_servico.codigo_os} - Item: {self.servico.nome} (Qtd: {self.quantidade})"

    def save(self, *args, **kwargs):
        # Calcula o valor total do item antes de salvar
        self.valor_total_item = self.quantidade * self.valor_unitario
        super().save(*args, **kwargs)

        # Atualiza o valor total da OrdemServico principal
        
        self.ordem_servico.valor_total = sum(item.valor_total_item for item in self.ordem_servico.itens.all())
        self.ordem_servico.save(update_fields=['valor_total'])