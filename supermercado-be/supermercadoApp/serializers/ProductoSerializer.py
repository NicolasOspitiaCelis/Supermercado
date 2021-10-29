from supermercadoApp.models.productos import Producto
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['id', 'name', 'category', 'proveedor']
