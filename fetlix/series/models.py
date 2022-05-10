from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre cliente', max_length=40)
    email = models.EmailField('Email cliente', max_length=40)
    contraseña = models.CharField('Contraseña cliente', max_length=40)
    imagen = models.ImageField('Imagen')
    # lista_posts


class Empresa(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre empresa', max_length=40)
    descripcion = models.CharField('Descripcion de producto en post', max_length=100)
    email = models.EmailField('Email empresa', max_length=40)
    contraseña = models.CharField('Contraseña empresa', max_length=40)
    imagen = models.ImageField('Imagen')
    # lista_productos


class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre producto', max_length=40)
    descripcion = models.CharField('Descripcion de producto en empresa', max_length=500)
    imagen = models.ImageField('Imagen')
    precio = models.FloatField('Precio')
    num_likes = models.IntegerField('Likes', default=0)

    propietario = models.ForeignKey(to='Empresa', on_delete=models.CASCADE)
    # listado de comentarios(post)


# class Login(models.Model):


class Post_Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo del post', max_length=40)
    descripcion = models.CharField('Descripcion de producto en post', max_length=100)
    opinion = models.CharField('Opinion dada por el cliente', max_length=500)
    num_likes = models.IntegerField('Likes', default=0)

    propietario = models.ForeignKey(to='Cliente', on_delete=models.CASCADE)
    producto = models.ForeignKey(to='Producto', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo) + ' - ' + str(self.descripcion) + str(self.propietario.primary_key)
