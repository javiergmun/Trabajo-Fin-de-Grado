from rest_framework import serializers
from series.models import Producto

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField()
    descripcion = serializers.CharField()
    imagen = serializers.ImageField()
    precio = serializers.FloatField()
    fecha_creacion = serializers.DateTimeField()
    num_likes = serializers.IntegerField()
    categoria = serializers.CharField()
    empresa = serializers.CharField()

    class Meta:
        model = Producto
        fields = '__all__'
