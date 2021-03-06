from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.utils.timezone import now


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name='Nombre cliente', max_length=40)
    email = models.EmailField(verbose_name='Email cliente', max_length=40, unique=True)
    imagen = models.ImageField(verbose_name='Imagen', upload_to='series/static/img/imagenes_clientes', blank=True)
    fecha_creacion = models.DateTimeField("Fecha de creacion", default=now, blank=True)

    def __str__(self):
        return str(self.nombre)

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name='Nombre de empresa', max_length=40, unique=True)
    descripcion = models.CharField(verbose_name='Descripcion de empresa', max_length=100)
    email = models.EmailField(verbose_name='Email empresa', max_length=40, unique=True)
    imagen = models.ImageField(verbose_name='Imagen corporativa de la empresa', upload_to='series/static/img/imagenes_empresa', blank=True)
    fecha_creacion = models.DateTimeField("Fecha de creacion", default=now, blank=True)

    def __str__(self):
        return self.nombre

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
    nombre = models.CharField(verbose_name='Nombre producto', max_length=25,unique=True)
    descripcion = models.CharField(verbose_name='Descripcion del producto (facilitado por la empresa)', max_length=300)
    imagen = models.ImageField(verbose_name='Imagen del producto', upload_to='series/static/img/imagenes_producto',default='series/static/img/imagenes_producto/no-product-image.png', blank=True)
    precio = models.CharField(verbose_name='Precio del producto',default="Sin precio",max_length=10, blank= True, null=True)
    fecha_creacion = models.DateTimeField("Fecha de creacion", default=now, blank=True)
    num_likes = models.IntegerField(verbose_name='Likes', default=0)
    categoria = models.SmallIntegerField(verbose_name='Categoria Producto',choices=CATEGORIA_ELECCION, default=SERVICIOS )

    empresa = models.ForeignKey(Empresa , related_name="productos", on_delete=models.CASCADE)

    #metadatos nombre de la clase y como aparecen en la bbdd
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['categoria']

    def __str__(self):
        return str(self.nombre)

    @property #decorador dice que no recibe parametros externos, se trata como un campo que no se guarda en la bbdd
    def is_famous(self):
        return self.num_likes > 5

class Post_Cliente(models.Model):
    #comentario

    id = models.AutoField(primary_key=True)
    opinion = models.CharField('Opinion dada por el cliente', max_length=500, blank= True)
    fecha_creacion = models.DateTimeField("Fecha de creacion", default=now, blank=True)

    cliente = models.ForeignKey(Cliente,related_name="propietario", on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, related_name="comentario", on_delete=models.CASCADE, null=True)


    def __str__(self):
        return str(self.producto) + ' - ' + str(self.cliente)
