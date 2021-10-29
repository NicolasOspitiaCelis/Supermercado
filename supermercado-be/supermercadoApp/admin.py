from django.contrib import admin
from .models.user import User
from .models.proveedores import Proveedor
from .models.productos import Producto
from .models.inventario import Inventario

# Register your models here.

admin.site.register(User)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Inventario)
