from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.utils.timezone import now


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name='Nombre cliente', max_length=40)
    email = models.EmailField(verbose_name='Email cliente', max_length=40, unique=True)
    contrasena = models.CharField(verbose_name='Contraseña cliente', max_length=40)
    imagen = models.ImageField(verbose_name='Imagen', upload_to='imagenes_cliente/', blank=True)
    fecha_creacion = models.DateTimeField("Fecha de creacion", default=now, blank=True)

    def __str__(self):
        return str(self.nombre) + ' - ' + str(self.email) + ' - ' + str(self.fecha_creacion)

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name='Nombre empresa', max_length=40, unique=True)
    descripcion = models.CharField(verbose_name='Descripcion de producto en post', max_length=100)
    email = models.EmailField(verbose_name='Email empresa', max_length=40, unique=True)
    contrasena = models.CharField(verbose_name='Contraseña empresa', max_length=40)
    imagen = models.ImageField(verbose_name='Imagen', upload_to='imagenes_empresa/', blank=True)
    fecha_creacion = models.DateTimeField("Fecha de creacion", default=now, blank=True)

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):

    COMIDA=1
    HOGAR=2
    INFORMATICA=3
    MODA=4
    SERVICIOS=5
    VEHICULOS=6
    OTROS=7

    CATEGORIA_ELECCION= (
        (COMIDA,"Comida"),
        (HOGAR,"Hogar"),
        (INFORMATICA,"Informatica"),
        (MODA,"Moda"),
        (SERVICIOS,"Servicios"),
        (VEHICULOS,"Vehiculos"),
        (OTROS,"Otros"),
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name='Nombre producto', max_length=40)
    descripcion = models.CharField(verbose_name='Descripcion de producto en empresa', max_length=500)
    imagen = models.ImageField(verbose_name='Imagen', upload_to='series/static/img/imagenes_producto', blank=True)
    precio = models.FloatField(verbose_name='Precio', blank= True)
    fecha_creacion = models.DateTimeField("Fecha de creacion", default=now, blank=True)
    num_likes = models.IntegerField(verbose_name='Likes', default=0)
    categoria = models.SmallIntegerField(verbose_name='Categoria Producto',choices=CATEGORIA_ELECCION, default=SERVICIOS )

    empresa = models.ForeignKey(Empresa,related_name="productos", on_delete=models.CASCADE)

    #metadatos nombre de la clase y como aparecen en la bbdd
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['categoria']

    def __str__(self):
        return str(self.nombre) + ' - ' + str(self.fecha_creacion) + ' - ' + str(self.empresa)+ ' - ' + str(self.categoria)

    @property #decorador dice que no recibe parametros externos, se trata como un campo que no se guarda en la bbdd
    def is_famous(self):
        return self.num_likes > 5

class Post_Cliente(models.Model):

    COMIDA=1
    HOGAR=2
    INFORMATICA=3
    MODA=4
    SERVICIOS=5
    VEHICULOS=6
    OTROS=7

    CATEGORIA_ELECCION= (
        (COMIDA,"Comida"),
        (HOGAR,"Hogar"),
        (INFORMATICA,"Informatica"),
        (MODA,"Moda"),
        (SERVICIOS,"Servicios"),
        (VEHICULOS,"Vehiculos"),
        (OTROS,"Otros"),
    )

    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo del post', max_length=40)
    descripcion = models.CharField('Descripcion de producto en post', max_length=100)
    opinion = models.CharField('Opinion dada por el cliente', max_length=500, blank= True)
    num_likes = models.IntegerField('Likes', default=0, blank=True)
    imagen = models.ImageField(verbose_name='Imagen' ,upload_to='imagenes_post/', blank=True)
    fecha_creacion = models.DateTimeField("Fecha de creacion", default=now, blank=True)
    categoria = models.SmallIntegerField(verbose_name='Categoria Post',choices=CATEGORIA_ELECCION, default=SERVICIOS, blank=True)


    cliente = models.ForeignKey(Cliente,related_name="post_cliente", on_delete=models.CASCADE)


    def __str__(self):
        return str(self.titulo) + ' - ' + str(self.fecha_creacion) + ' - ' + str(self.cliente)
