from rest_framework import serializers
from api.models import *

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class EstacionamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacionamiento
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

