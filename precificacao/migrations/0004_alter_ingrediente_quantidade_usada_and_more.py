# Generated by Django 4.2.5 on 2023-09-20 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precificacao', '0003_ingrediente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='quantidade_usada',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='valor_embalagem',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]
