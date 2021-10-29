from django.db import models
from .proveedores import Proveedor


class Producto(models.Model):
    id = models.AutoField('id', primary_key=True)
    proveedor = models.ForeignKey(
        Proveedor, related_name='proveedor', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=100)
    category = models.CharField('category', max_length=40)
