from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad_stock',]

# validaciones

# nombre
def clean_nombre(self):
    nombre = self.cleaned_data.get('nombre')
    if nombre and len(nombre) < 3:
        raise forms.ValidationError("El nombre debe tener al menos 3 caracteres")
    return nombre

# descripcion
def clean_descripcion(self):
    descripcion = self.cleaned_data.get('descripcion')
    if descripcion and len(descripcion) < 10:
        raise forms.ValidationError("La descripcion debe tener al menos 10 caracteres")
    return descripcion

# precio
def clean_precio(self):
    precio = self.cleaned_data.get('precio')
    if precio is not None and precio <= 0:
        raise forms.ValidationError("El precio debe ser mayor a 0")
    return precio

# cantidad_stock
def clean_cantidad_stock(self):
    cantidad_stock = self.cleaned_data.get('cantidad_stock')
    if cantidad_stock is not None and cantidad_stock < 0:
        raise forms.ValidationError("La cantidad de stock debe ser mayor a 0")
    return cantidad_stock
