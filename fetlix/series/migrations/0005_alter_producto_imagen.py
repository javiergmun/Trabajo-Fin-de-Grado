# Generated by Django 4.0.3 on 2022-05-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0004_alter_post_cliente_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='series/ststic/img/imagenes_producto', verbose_name='Imagen'),
        ),
    ]