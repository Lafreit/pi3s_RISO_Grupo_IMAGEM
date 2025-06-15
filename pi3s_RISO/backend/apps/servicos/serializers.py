# apps/servicos/serializers.py
from rest_framework import serializers
from .models import Servico

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__' # Ou especifique uma tupla como: ('id', 'codigo_servico', ...)
        read_only_fields = ('data_criacao', 'data_atualizacao') # Estes campos são definidos automaticamente

    def validate(self, data):
        # Validação ID 4.2.1 (se 'Outro' for selecionado, tipo_servico_outro deve ser preenchido)
        if data.get('tipo_servico') == 'O' and not data.get('tipo_servico_outro'):
            raise serializers.ValidationError(
                {"tipo_servico_outro": "Por favor, especifique o tipo do serviço quando 'Outro' for selecionado."}
            )
        elif data.get('tipo_servico') != 'O' and data.get('tipo_servico_outro'):
            # Se um tipo específico foi selecionado, o campo 'tipo_servico_outro' deve estar vazio
            # Isso é para evitar dados inconsistentes
            data['tipo_servico_outro'] = None

        # As validações de MinValueValidator já estão no model,
        # mas aqui você pode adicionar validações mais complexas se necessário.
        return data