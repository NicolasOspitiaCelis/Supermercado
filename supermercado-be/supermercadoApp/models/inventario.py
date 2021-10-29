from django.db import models
from .productos import Producto


class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(
        Producto, related_name='inventario', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=100)
    category = models.CharField('category', max_length=40)
    amount = models.IntegerField('amount')
