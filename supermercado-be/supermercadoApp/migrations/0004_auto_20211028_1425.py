# Generated by Django 3.2.7 on 2021-10-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermercadoApp', '0003_alter_compra_inventario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='inventario',
        ),
        migrations.AddField(
            model_name='compra',
            name='inventario_id',
            field=models.IntegerField(default=0, verbose_name='inventario_id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='name',
            field=models.CharField(default=0, max_length=50, verbose_name='name'),
            preserve_default=False,
        ),
    ]