from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import  render, redirect, get_object_or_404
from django.core.paginator import Paginator


# REED, CREATE, UDPATE, DELETE (CRUD)
# Listamos los productos
def listar_productos(request):
    busqueda = request.GET.get('busqueda')

    if busqueda:
        productos = Producto.objects.filter(nombre__icontains=busqueda)
    else:
        productos = Producto.objects.all()

    paginator = Paginator(productos, 5)
    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)

    return render(request, 'productos/listar_productos.html', {
        'productos': productos,
        'busqueda': busqueda
    })

# Metodo crear
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()

    return render(request, 'productos/crear_producto.html', {'form': form})

# Actualizar producto
def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/actualizar_producto.html', {'form': form})

# Elimnar un producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})





