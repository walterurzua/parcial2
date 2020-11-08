from django.contrib import admin
from .models import registro, Productos
# Register your models here.
class Productosadmin(admin.ModelAdmin):
    list_display = ("id", "nombrep", "descripcion", "img", "stock", "precioCosto", "precioVenta")

admin.site.register(registro)
admin.site.register(Productos,Productosadmin)

