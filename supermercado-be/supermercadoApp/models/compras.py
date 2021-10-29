from django.db import models


class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    inventario_id = models.IntegerField('inventario_id')
    name = models.CharField('name', max_length=50)
    amountC = models.IntegerField('amount')
