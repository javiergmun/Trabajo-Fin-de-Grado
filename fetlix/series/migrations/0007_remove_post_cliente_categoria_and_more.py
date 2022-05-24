# Generated by Django 4.0.3 on 2022-05-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0006_alter_post_cliente_titulo_alter_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_cliente',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='post_cliente',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='post_cliente',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='post_cliente',
            name='num_likes',
        ),
        migrations.AlterField(
            model_name='empresa',
            name='descripcion',
            field=models.CharField(max_length=100, verbose_name='Descripcion de empresa'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='imagenes_empresa/', verbose_name='Imagen corporativa de la empresa'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(max_length=40, unique=True, verbose_name='Nombre de empresa'),
        ),
        migrations.AlterField(
            model_name='post_cliente',
            name='titulo',
            field=models.CharField(max_length=25, verbose_name='Nombre del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=300, verbose_name='Descripcion del producto (facilitado por la empresa)'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='series/static/img/imagenes_producto', verbose_name='Imagen del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(blank=True, verbose_name='Precio del producto'),
        ),
    ]