from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.context_processors import request
from django_filters import filters
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from series.serializers import ProductSerializer, ClienteSerializer, EmpresaSerializer, \
    PostSerializer_GET, PostSerializer_POST, ClienteSerializer_POST, ProductSerializer_Post

from django.views import View
from series.models import Producto, Post_Cliente, Cliente, Empresa
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


########################################################
#                                                      #
#                ENDPOINTS PRODUCTOS                   #
#                                                      #
########################################################
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def ProductList(request, format=None):
    # Listar productos o crear productos
    if request.method == 'GET':
        producto = Producto.objects.all().order_by('-num_likes')
        serializer = ProductSerializer(producto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer_Post(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Producto_por_nombre(request, nombre, format=None):
    try:
        producto = Producto.objects.get(nombre=nombre)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(producto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        producto.delete(nombre=nombre)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Producto_de_una_empresaID(request, empresa_id, format=None):
    try:
        producto = Producto.objects.filter(empresa_id=empresa_id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(producto, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        producto.delete(empresa_id=empresa_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductList_COMIDA(APIView):
    permission_classes = [IsAuthenticated]

    # Listar productos o crear productos
    def get(self, request, format=None):
        productos = Producto.objects.all().filter(categoria=1)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductList_HOGAR(APIView):
    permission_classes = [IsAuthenticated]

    # Listar productos o crear productos
    def get(self, request, format=None):
        productos = Producto.objects.all().filter(categoria=2)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductList_INFORMATICA(APIView):
    permission_classes = [IsAuthenticated]

    # Listar productos o crear productos
    def get(self, request, format=None):
        productos = Producto.objects.all().filter(categoria=3)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductList_MODA(APIView):
    permission_classes = [IsAuthenticated]

    # Listar productos o crear productos
    def get(self, request, format=None):
        productos = Producto.objects.all().filter(categoria=4)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductList_SERVICIOS(APIView):
    permission_classes = [IsAuthenticated]

    # Listar productos o crear productos
    def get(self, request, format=None):
        productos = Producto.objects.all().filter(categoria=5)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductList_VEHICULOS(APIView):
    permission_classes = [IsAuthenticated]

    # Listar productos o crear productos
    def get(self, request, format=None):
        productos = Producto.objects.all().filter(categoria=6)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductList_OTROS(APIView):
    permission_classes = [IsAuthenticated]

    # Listar productos o crear productos
    def get(self, request, format=None):
        productos = Producto.objects.all().filter(categoria=7)
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductList_ORDER_BY_LIKES(APIView):
    permission_classes = [IsAuthenticated]

    # Listar productos o crear productos
    def get(self, request, format=None):
        productos = Producto.objects.all().order_by('-num_likes')
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


########################################################
#                                                      #
#                   ENDPOINTS POSTS                    #
#                                                      #
########################################################
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def PostList(request, format=None):
    # Listar comentarios o crear comentarios
    if request.method == 'GET':
        post = Post_Cliente.objects.all()
        serializer = PostSerializer_GET(post, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        coment_data = JSONParser().parse(request)
        serializer = PostSerializer_POST(data=coment_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Post_de_un_productoID(request, producto_id, format=None):
    try:
        post = Post_Cliente.objects.filter(producto_id=producto_id)
    except Post_Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer_GET(post, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer_POST(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete(producto_id=producto_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Post_de_un_clienteID(request, cliente_id, format=None):
    try:
        post = Post_Cliente.objects.filter(cliente_id=cliente_id)
    except Post_Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer_GET(post, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer_POST(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete(cliente_id=cliente_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


########################################################
#                                                      #
#                ENDPOINTS CLIENTES                    #
#                                                      #
########################################################
class ClienteList(APIView):
    permission_classes = [IsAuthenticated]

    # Listar cliente o crear cliente
    def get(self, request, format=None):
        posts = Cliente.objects.all()
        serializer = ClienteSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def PostCliente(request, format=None):

    if request.method == 'POST':
        cliente_data = JSONParser().parse(request)
        serializer = ClienteSerializer_POST(data=cliente_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Cliente_por_nombre(request, nombre, format=None):
    try:
        cliente = Cliente.objects.get(nombre=nombre)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cliente.delete(nombre=nombre)
        return Response(status=status.HTTP_204_NO_CONTENT)


########################################################
#                                                      #
#               ENDPOINTS EMPRESA                      #
#                                                      #
########################################################
class EmpresaList(APIView):
    # Listar empresa o crear empresa
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        posts = Empresa.objects.all()
        serializer = EmpresaSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Empresa_por_nombre(request, nombre, format=None):
    try:
        empresa = Empresa.objects.get(nombre=nombre)
    except Empresa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmpresaSerializer(empresa)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmpresaSerializer(empresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        empresa.delete(nombre=nombre)
        return Response(status=status.HTTP_204_NO_CONTENT)


########################################################
#                                                      #
#               MOTOR DE BUSCADOR                      #
#                                                      #
########################################################
def busqueda(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    if queryset:
        eventos = Producto.objects.filter(
            Q(descripcion__icontains=queryset)
        ).distinct()
    return render(request, 'index.html', {'eventos': eventos})


########################################################
#                                                      #
#               Registro usuario                       #
#                                                      #
########################################################

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})
########################################################
#                                                      #
#              ENDPOINTS VISTAS HTML                   #
#                                                      #
########################################################
class Inicio(View):
    def get(self, request):
        return render(request, 'index.html')


class Perfil(View):
    def get(self, request):
        return render(request, 'perfil.html')


##TODO VIEW PUNTUAL
class Registro(View):
    def get(self, request):
        return render(request, 'registro.html')


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
