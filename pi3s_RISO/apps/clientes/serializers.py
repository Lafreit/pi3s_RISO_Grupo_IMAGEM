# apps/clientes/serializers.py
from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' # Inclui todos os campos do modelo Cliente
        # Ou você pode listar os campos explicitamente:
        # fields = [
        #     'id', 'nome_completo', 'tipo', 'cpf', 'cnpj', 'cep', 'rua',
        #     'numero', 'complemento', 'bairro', 'cidade', 'estado',
        #     'telefone_principal', 'telefone_secundario', 'email',
        #     'data_cadastro', 'ativo'
        # ]
        read_only_fields = ('data_cadastro',) # data_cadastro é gerada automaticamente

        # apps/autenticacao/serializers.py

