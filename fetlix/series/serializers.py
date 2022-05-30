from rest_framework import serializers
from series.models import Producto, Post_Cliente, Cliente, Empresa


class ProductSerializer(serializers.ModelSerializer):
    empresa= serializers.StringRelatedField()

    class Meta:
        model = Producto
        fields = ('id','nombre','descripcion','imagen','precio','fecha_creacion','num_likes','categoria','empresa')
        #fields = ('__all__')


class PostSerializer_GET(serializers.ModelSerializer):
    producto = serializers.StringRelatedField()
    cliente = serializers.StringRelatedField()

    class Meta:
        model = Post_Cliente
        fields= ('id','opinion','fecha_creacion','cliente','producto')

class PostSerializer_POST(serializers.ModelSerializer):

    class Meta:
        model = Post_Cliente
        fields= ('id','opinion','fecha_creacion','cliente','producto')


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields=('__all__')

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields=('__all__')