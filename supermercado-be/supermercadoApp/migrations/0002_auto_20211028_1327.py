# Generated by Django 3.2.7 on 2021-10-28 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermercadoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proveedor', to='supermercadoApp.proveedor'),
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amountC', models.IntegerField(verbose_name='amount')),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario', to='supermercadoApp.inventario')),
            ],
        ),
    ]
