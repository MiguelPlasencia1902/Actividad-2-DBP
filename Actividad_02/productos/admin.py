from django.contrib import admin
from .models import Producto

# Register your models here.

admin.site.register(Producto)

def __str__(self):
    return self.nombre