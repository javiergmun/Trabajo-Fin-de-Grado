# Generated by Django 4.0.3 on 2022-05-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0007_remove_post_cliente_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(blank=True, null=True, verbose_name='Precio del producto'),
        ),
    ]
