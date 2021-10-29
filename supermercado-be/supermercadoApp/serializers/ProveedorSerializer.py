from supermercadoApp.models.proveedores import Proveedor
from rest_framework import serializers


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['id', 'name']
