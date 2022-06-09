"""fetlix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from series import views

from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion oficial API",
      default_version='v1',
      description="Documentación de la API TFG",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="soporte@opinionestfg.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    ##### ADMINISTRADOR #####
    path('admin/', admin.site.urls, name="administrator"),

    ##### CATEGORIAS MENU 1.0 #####
    path('categorias/', include('series.urls')),

    ##### ENDPOINTS #####
    path('productos/', include('series.urls')),
    path('posts/', include('series.urls')),
    path('empresas/', include('series.urls')),
    path('clientes/', include('series.urls')),

    ##### BASE / RAIZ #####
    path('',TemplateView.as_view(template_name='index.html'),name='home'),

    ##### LOGIN / REGISTRO / AUTENTIFICACION #####
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),

    #### AUTH
    path('login/', obtain_jwt_token),

    ##Registro
    url(r'^signup/$', views.signup, name='signup'),

    path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='download-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






# AUTENTIFICACION (URLS QUE IMPORTA)
# ^accounts/login/$ [name='login']
# ^accounts/logout/$ [name='logout']
# ^accounts/password_change/$ [name='password_change']
# ^accounts/password_change/done/$ [name='password_change_done']
# ^accounts/password_reset/$ [name='password_reset']
# ^accounts/password_reset/done/$ [name='password_reset_done']
# ^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
# ^accounts/reset/done/$ [name='password_reset_complete']


