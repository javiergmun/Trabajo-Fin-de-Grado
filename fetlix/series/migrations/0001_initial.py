# Generated by Django 4.0.3 on 2022-05-11 20:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre cliente')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='Email cliente')),
                ('contrasena', models.CharField(max_length=40, verbose_name='Contraseña cliente')),
                ('imagen', models.ImageField(blank=True, upload_to='imagenes_cliente/', verbose_name='Imagen')),
                ('fecha_creacion', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Fecha de creacion')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, unique=True, verbose_name='Nombre empresa')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion de producto en post')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='Email empresa')),
                ('contrasena', models.CharField(max_length=40, verbose_name='Contraseña empresa')),
                ('imagen', models.ImageField(blank=True, upload_to='imagenes_empresa/', verbose_name='Imagen')),
                ('fecha_creacion', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Fecha de creacion')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre producto')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripcion de producto en empresa')),
                ('imagen', models.ImageField(blank=True, upload_to='', verbose_name='Imagen')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('fecha_creacion', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Fecha de creacion')),
                ('num_likes', models.IntegerField(default=0, verbose_name='Likes')),
                ('categoria', models.SmallIntegerField(choices=[(1, 'Comida'), (2, 'Hogar'), (3, 'Informatica'), (4, 'Moda'), (5, 'Servicios'), (6, 'Vehiculos'), (7, 'Otros')], default=5, verbose_name='Categoria Producto')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='series.empresa')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['categoria'],
            },
        ),
        migrations.CreateModel(
            name='Post_Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=40, verbose_name='Titulo del post')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion de producto en post')),
                ('opinion', models.CharField(max_length=500, verbose_name='Opinion dada por el cliente')),
                ('num_likes', models.IntegerField(default=0, verbose_name='Likes')),
                ('imagen', models.ImageField(blank=True, upload_to='', verbose_name='Imagen')),
                ('fecha_creacion', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Fecha de creacion')),
                ('categoria', models.SmallIntegerField(choices=[(1, 'Comida'), (2, 'Hogar'), (3, 'Informatica'), (4, 'Moda'), (5, 'Servicios'), (6, 'Vehiculos'), (7, 'Otros')], default=5, verbose_name='Categoria Post')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_cliente', to='series.cliente')),
            ],
        ),
    ]
