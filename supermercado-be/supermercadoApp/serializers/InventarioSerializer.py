from supermercadoApp.models.inventario import Inventario
from rest_framework import serializers


class InventarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventario
        fields = ['id', 'name', 'category', 'amount', 'producto']
