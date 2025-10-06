from django.contrib import admin

# Register your models here.

from .models import clientes
# registrar el modelo alumno en el admin
admin.site.register(clientes)

