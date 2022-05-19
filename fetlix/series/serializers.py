from rest_framework import serializers
from series.models import Producto, Post_Cliente, Cliente, Empresa


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField()
    descripcion = serializers.CharField()
    imagen = serializers.ImageField(allow_null=True)
    precio = serializers.FloatField()
    fecha_creacion = serializers.DateTimeField()
    num_likes = serializers.IntegerField()
    categoria = serializers.CharField()
    empresa = serializers.CharField()

    class Meta:
        model = Producto

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField()
    descripcion = serializers.CharField()
    fecha_creacion = serializers.DateTimeField()
    num_likes = serializers.IntegerField()
    categoria = serializers.CharField()

    class Meta:
        model = Post_Cliente

class ClienteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField()
    email = serializers.EmailField()
    imagen = serializers.ImageField(allow_null=True)
    fecha_creacion = serializers.DateTimeField()

    class Meta:
        model = Cliente

class EmpresaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField()
    descripcion = serializers.CharField()
    email = serializers.EmailField()
    imagen = serializers.ImageField(allow_null=True)
    fecha_creacion = serializers.DateTimeField()

    class Meta:
        model = Empresa

