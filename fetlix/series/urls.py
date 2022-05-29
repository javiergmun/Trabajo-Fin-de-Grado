from django.contrib.auth import login
from django.template.defaulttags import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from series import views
from django.urls import path, include

from series.views import Perfil

urlpatterns = [
    ##### ENDPOINTS PERFIL 2.0 ##### TODO CAMBIARLO A LAS URL BASE YA QUE NO DEPENDE DE NADIE
    path('perfil', views.Perfil.as_view(), name="perfil"),

    ##### CATEGORIAS MENU 2.0 #####
    path('comida',views.Comida.as_view(), name="comida"),
    path('moda',views.Moda.as_view(), name="moda"),
    path('informatica',views.Informatica.as_view(), name="informatica"),
    path('hogar',views.Hogar.as_view(), name="hogar"),
    path('vehiculos',views.Vehiculos.as_view(), name="vehiculos"),
    path('servicios',views.Servicios.as_view(), name="servicios"),

    ##### ENDPOINTS PRODUCTO 2.0 #####
    path('producto/', views.ProductList, name="productos_lista"),
    path('producto/<str:nombre>', views.ProductDetalle, name="productos_detalles"),

    ##### ENDPOINTS POST 2.0 #####
    path('post/', views.PostList, name="post_lista"),
    path('post/<str:producto>', views.PostDetalle, name="post_detalles"),

    ##### ENDPOINTS CLIENTE 2.0 #####
    path('cliente/', views.ClienteList.as_view(), name="cliente_lista"),

    ##### ENDPOINTS EMPRESA 2.0 #####
    path('empresa/', views.EmpresaList.as_view(), name="empresa_lista"),

    ##### ENDPOINTS CATEGORIA COMIDA 2.0 #####
    path('comida/', views.ProductList_COMIDA.as_view(), name="cat_comida_lista"),

    ##### ENDPOINTS CATEGORIA HOGAR 2.0 #####
    path('hogar/', views.ProductList_HOGAR.as_view(), name="cat_hogar_lista"),

    ##### ENDPOINTS CATEGORIA INFORMATICA 2.0 #####
    path('informatica/', views.ProductList_INFORMATICA.as_view(), name="cat_informatica_lista"),

    ##### ENDPOINTS CATEGORIA MODA 2.0 #####
    path('moda/', views.ProductList_MODA.as_view(), name="cat_modalista"),

    ##### ENDPOINTS CATEGORIA SERVICIOS 2.0 #####
    path('servicios/', views.ProductList_SERVICIOS.as_view(), name="cat_servicios_lista"),

    ##### ENDPOINTS CATEGORIA VEHICULOS 2.0 #####
    path('vehiculos/', views.ProductList_VEHICULOS.as_view(), name="empresa_lista"),

    path('ord_likes/', views.ProductList_ORDER_BY_LIKES.as_view(), name="empresa_lista"),
    path('ord_likes/', views.ProductList_ORDER_BY_LIKES.as_view(), name="empresa_lista"),


]
urlpatterns = format_suffix_patterns(urlpatterns)