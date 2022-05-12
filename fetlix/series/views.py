from django.http import HttpResponse
from django.shortcuts import render

from django.views import View
from series.models import Producto


#def producto_lista(request):
 #   context = {
  #      'lista_productos': Producto.objects.all()
   # }
    #return render(request, 'producto_lista.html', context)


#def producto_detalle_vista(request, pk):
 #   context = {
  #      'pk': pk
   # }
    #return render(request, 'producto_detalle_vista.html', context)



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
