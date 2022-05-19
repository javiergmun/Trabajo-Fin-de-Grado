from django.http import HttpResponse
from django.shortcuts import render
from django_filters import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from series.serializers import ProductSerializer, PostSerializer, ClienteSerializer, EmpresaSerializer

from django.views import View
from series.models import Producto, Post_Cliente, Cliente, Empresa


class ProductList(APIView):
    #Listar productos o crear productos
    def get(self, request , format=None):
        productos= Producto.objects.all()
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def post(self,request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductList_COMIDA(APIView):
    #Listar productos o crear productos
    def get(self, request , format=None):
        productos= Producto.objects.all().filter(categoria=1)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
class ProductList_HOGAR(APIView):
    #Listar productos o crear productos
    def get(self, request , format=None):
        productos= Producto.objects.all().filter(categoria=2)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
class ProductList_INFORMATICA(APIView):
    #Listar productos o crear productos
    def get(self, request , format=None):
        productos= Producto.objects.all().filter(categoria=3)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
class ProductList_MODA(APIView):
    #Listar productos o crear productos
    def get(self, request , format=None):
        productos= Producto.objects.all().filter(categoria=4)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
class ProductList_SERVICIOS(APIView):
    #Listar productos o crear productos
    def get(self, request , format=None):
        productos= Producto.objects.all().filter(categoria=5)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
class ProductList_VEHICULOS(APIView):
    #Listar productos o crear productos
    def get(self, request , format=None):
        productos= Producto.objects.all().filter(categoria=6)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
class ProductList_OTROS(APIView):
    #Listar productos o crear productos
    def get(self, request , format=None):
        productos= Producto.objects.all().filter(categoria=7)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
class ProductList_ORDER_BY_LIKES(APIView):
    #Listar productos o crear productos
    def get(self, request , format=None):
        productos= Producto.objects.all().order_by('-num_likes')
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

class PostList(APIView):
    #Listar posts o crear posts TODOS
    def get(self, request , format=None):
        posts = Post_Cliente.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteList(APIView):
    #Listar cliente o crear cliente
    def get(self, request , format=None):
        posts = Cliente.objects.all().filter()
        serializer = ClienteSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpresaList(APIView):
    #Listar empresa o crear empresa
    def get(self, request , format=None):
        posts = Empresa.objects.all()
        serializer = EmpresaSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Inicio(View):
    def get(self, request):
        return render(request, 'index.html')


class Perfil(View):
    def get(self, request):
        return render(request, 'perfil.html')


class Comida(View):
    def get(self, request):
        return render(request, 'categoria-comida.html')


class Hogar(View):
    def get(self, request):
        return render(request, 'categoria-hogar.html')


class Informatica(View):
    def get(self, request):
        return render(request, 'categoria-informatica.html')


class Moda(View):
    def get(self, request):
        return render(request, 'categoria-moda.html')


class Servicios(View):
    def get(self, request):
        return render(request, 'categoria-servicios.html')


class Vehiculos(View):
    def get(self, request):
        return render(request, 'categoria-vehiculos.html')
