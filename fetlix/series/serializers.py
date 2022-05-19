from rest_framework import serializers
from series.models import Producto, Post_Cliente, Cliente, Empresa


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','nombre','descripcion','imagen','precio','fecha_creacion','num_likes','categoria','empresa')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Cliente
        fields= ('__all__')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields=('__all__')

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields=('__all__')

