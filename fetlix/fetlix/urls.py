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
    path('',Inicio.as_view(), include('series.urls')),
    path('perfil.html/',Perfil.as_view()),
    path('categoria-comida.html/',Comida.as_view()),
    path('categoria-moda.html/',Moda.as_view()),
    path('categoria-hogar.html/',Hogar.as_view()),
    path('categoria-informatica.html/',Informatica.as_view()),
    path('categoria-servicios.html/',Servicios.as_view()),
    path('categoria-vehiculos.html/',Vehiculos.as_view()),
    path('productos/', include('series.urls'))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
