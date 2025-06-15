# apps/departamentos/serializers.py
from rest_framework import serializers
from .models import Departamento # Assumindo que você tem um modelo Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'