# C:\pi3s\pi3s_RISO\backend\apps\clientes\serializers.py

from rest_framework import serializers
from .models import Cliente
# Importar os validadores customizados, se já os tiver
# from .validators import validate_cpf, validate_cnpj, validate_cep, validate_min_length_for_name

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' # Inclui todos os campos do modelo Cliente

    # Aqui você pode adicionar validações extras ou métodos para integração com API de CEP (ID 2.2.2)
    # def validate_nome_completo_razao_social(self, value): # ID 2.1.3
    #     if len(value) < 3: # Exemplo de validação de mínimo de caracteres
    #         raise serializers.ValidationError("O nome completo/razão social deve ter no mínimo 3 caracteres.")
    #     return value

    # def validate_cpf(self, value): # ID 2.3.2
    #     # Use a função de validação de CPF
    #     validate_cpf(value)
    #     return value

    # def validate_cnpj(self, value): # ID 2.3.3
    #     # Use a função de validação de CNPJ
    #     validate_cnpj(value)
    #     return value

    # def validate_cep(self, value): # ID 2.2.3
    #     # Use a função de validação de CEP
    #     validate_cep(value)
    #     return value

    # def create(self, validated_data):
    #     # Lógica para integração com API de CEP ao criar
    #     # if 'cep' in validated_data and validated_data['cep']:
    #     #     # Chamar a função de preenchimento de endereço
    #     #     # cliente = super().create(validated_data)
    #     #     # cliente.preencher_endereco_por_cep()
    #     #     # cliente.save()
    #     #     pass
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     # Lógica para integração com API de CEP ao atualizar
    #     # if 'cep' in validated_data and validated_data['cep']:
    #     #     # instance.cep = validated_data['cep']
    #     #     # instance.preencher_endereco_por_cep()
    #     #     pass
    #     return super().update(instance, validated_data)