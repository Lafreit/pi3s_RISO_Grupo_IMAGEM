# apps/empregados/serializers.py
from rest_framework import serializers
from .models import Empregado, Departamento # Importe Empregado e Departamento

class EmpregadoSerializer(serializers.ModelSerializer):
    # Campo para exibir o nome do departamento em vez do ID (leitura)
    departamento_nome = serializers.CharField(source='departamento.nome', read_only=True)

    class Meta:
        model = Empregado
        fields = '__all__'
        read_only_fields = ['codigo_empregado', 'data_cadastro', 'data_atualizacao']

    # Validação para garantir que o departamento existe (se fornecido)
    def validate_departamento(self, value):
        if value and not Departamento.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError("Departamento não encontrado.")
        return value