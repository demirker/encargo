# Generated by Django 4.2.1 on 2023-06-12 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codigo', '0005_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(blank=True, verbose_name='Precio del producto'),
        ),
    ]
