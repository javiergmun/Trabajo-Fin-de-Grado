from django.contrib.auth import login
from django.template.defaulttags import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from series import views
from django.urls import path, include



urlpatterns = [
    path('producto/', views.ProductList.as_view(), name="productos_lista"),
    path('post/', views.PostList.as_view(), name="post_lista"),
    path('cliente/', views.ClienteList.as_view(), name="cliente_lista"),
    path('empresa/', views.EmpresaList.as_view(), name="empresa_lista"),
    path('comida/', views.ProductList_COMIDA.as_view(), name="empresa_lista"),
    path('hogar/', views.ProductList_HOGAR.as_view(), name="empresa_lista"),
    path('informatica/', views.ProductList_INFORMATICA.as_view(), name="empresa_lista"),
    path('moda/', views.ProductList_MODA.as_view(), name="empresa_lista"),
    path('servicios/', views.ProductList_SERVICIOS.as_view(), name="empresa_lista"),
    path('vehiculos/', views.ProductList_VEHICULOS.as_view(), name="empresa_lista"),
    path('otros/', views.ProductList_OTROS.as_view(), name="empresa_lista"),
    path('ord_likes/', views.ProductList_ORDER_BY_LIKES.as_view(), name="empresa_lista"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
