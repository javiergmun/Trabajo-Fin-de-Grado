from django.contrib import admin

# Register your models here.
from series.models import Cliente, Post_Cliente, Empresa, Producto


admin.site.register(Cliente)
admin.site.register(Post_Cliente)
admin.site.register(Empresa)
admin.site.register(Producto)