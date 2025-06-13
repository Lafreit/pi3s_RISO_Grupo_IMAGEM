# apps/veiculos/serializers.py

from rest_framework import serializers
from .models import Veiculo # Importe o modelo Veiculo que acabamos de definir

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__' # Inclui todos os campos do modelo Veiculo
        # ou, se preferir listar explicitamente:
        # fields = [
        #     'id', 'tipo', 'placa', 'marca', 'modelo', 'ano_fabricacao',
        #     'quilometragem_atual', 'cor', 'observacoes',
        #     'data_cadastro', 'data_atualizacao'
        # ]
        read_only_fields = ['data_cadastro', 'data_atualizacao'] # Campos que não podem ser alterados via API