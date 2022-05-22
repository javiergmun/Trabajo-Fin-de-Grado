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
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.views.generic import TemplateView

from series.views import Inicio
from series.views import Perfil
from series.views import Comida
from series.views import Moda
from series.views import Hogar
from series.views import Informatica
from series.views import Servicios
from series.views import Vehiculos

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',Inicio.as_view()),
    path('',TemplateView.as_view(template_name='index.html'),name='home'),
    #path('perfil.html/',Perfil.as_view()),
    path('categoria-comida.html/',Comida.as_view()),
    path('categoria-moda.html/',Moda.as_view()),
    path('categoria-hogar.html/',Hogar.as_view()),
    path('categoria-informatica.html/',Informatica.as_view()),
    path('categoria-servicios.html/',Servicios.as_view()),
    path('categoria-vehiculos.html/',Vehiculos.as_view()),
    path('productos/', include('series.urls')),
    path('posts/', include('series.urls')),
    path('clientes/', include('series.urls')),
    path('empresas/', include('series.urls')),
    #AUTENTIFICACION (URLS QUE IMPORTA)
        #^accounts/login/$ [name='login']
        #^accounts/logout/$ [name='logout']
        #^accounts/password_change/$ [name='password_change']
        #^accounts/password_change/done/$ [name='password_change_done']
        #^accounts/password_reset/$ [name='password_reset']
        #^accounts/password_reset/done/$ [name='password_reset_done']
        #^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
        #^accounts/reset/done/$ [name='password_reset_complete']
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls'))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


