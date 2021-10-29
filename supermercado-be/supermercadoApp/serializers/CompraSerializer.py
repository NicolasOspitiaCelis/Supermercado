from supermercadoApp.models.compras import Compra
from rest_framework import serializers


class CompraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compra
        fields = ['id', 'inventario_id', 'name', 'amountC']
