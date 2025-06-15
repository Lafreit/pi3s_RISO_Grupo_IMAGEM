# apps/ordem_servico/serializers.py
from rest_framework import serializers
from .models import OrdemServico, ItemOrdemServico
# Importa os serializers dos apps relacionados para exibição detalhada
from apps.clientes.serializers import ClienteSerializer
from apps.veiculos.serializers import VeiculoSerializer
from apps.empregados.serializers import EmpregadoSerializer
from apps.servicos.serializers import ServicoSerializer

class ItemOrdemServicoSerializer(serializers.ModelSerializer):
    # Campo para exibir o nome do serviço em vez do ID, se houver um ServicoSerializer
    servico_nome = serializers.CharField(source='servico.nome', read_only=True)

    class Meta:
        model = ItemOrdemServico
        fields = '__all__'
        read_only_fields = ['valor_total_item'] # Calculado automaticamente

class OrdemServicoSerializer(serializers.ModelSerializer):
    # Campo para exibir informações detalhadas dos objetos relacionados (leitura)
    cliente_detalhes = ClienteSerializer(source='cliente', read_only=True)
    veiculo_detalhes = VeiculoSerializer(source='veiculo', read_only=True)
    empregado_responsavel_detalhes = EmpregadoSerializer(source='empregado_responsavel', read_only=True)

    # Campo aninhado para itens da ordem de serviço
    # Permite criar/atualizar itens junto com a ordem de serviço principal
    itens = ItemOrdemServicoSerializer(many=True, required=False)

    class Meta:
        model = OrdemServico
        fields = '__all__'
        read_only_fields = ['codigo_os', 'data_emissao', 'data_atualizacao', 'valor_total']

    # Método para criar a OrdemServico e seus ItemOrdemServico aninhados
    def create(self, validated_data):
        itens_data = validated_data.pop('itens', []) # Extrai os dados dos itens, se houver
        ordem_servico = OrdemServico.objects.create(**validated_data) # Cria a OrdemServico principal
        for item_data in itens_data:
            ItemOrdemServico.objects.create(ordem_servico=ordem_servico, **item_data) # Cria cada item
        return ordem_servico

    # Método para atualizar a OrdemServico e seus ItemOrdemServico aninhados
    def update(self, instance, validated_data):
        itens_data = validated_data.pop('itens', None) # Extrai os dados dos itens para atualização

        # Atualiza os campos da OrdemServico principal
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if itens_data is not None:
            # Lógica para atualizar/criar/deletar itens existentes
            instance.itens.all().delete() # Exclui todos os itens existentes
            for item_data in itens_data:
                ItemOrdemServico.objects.create(ordem_servico=instance, **item_data) # Recria todos os itens

        return instance