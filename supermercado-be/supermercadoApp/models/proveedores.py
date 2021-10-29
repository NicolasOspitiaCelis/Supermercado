from django.db import models


class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=100)
