from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


# class HelloWorld(View):
# def get(self, request):
# return HttpResponse(content=b'Hello World')

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
