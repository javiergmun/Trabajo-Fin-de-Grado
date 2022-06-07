from django.contrib import admin

# Register your models here.
from series.models import Cliente, Post_Cliente, Empresa, Producto


admin.site.register(Cliente)
admin.site.register(Post_Cliente)
#admin.site.register(Empresa)
#admin.site.register(Producto)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "empresa","num_likes","fecha_creacion")
    list_filter = ("categoria","empresa")
    search_fields = ("nombre__startswith",)


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nombre","email","fecha_creacion")
    search_fields = ("nombre__startswith",)

