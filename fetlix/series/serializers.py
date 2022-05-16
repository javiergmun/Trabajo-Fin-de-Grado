from rest_framework import serializers
from series.models import Producto

class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Producto
        fields = '__all__'