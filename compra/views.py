from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .forms import ProveedorForm, ProductoForm
from django.urls import reverse
from .models import Proveedor, Producto
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
from django.contrib import messages

app_name = "control"


# Create your views here.
def index(request):
    return render(request, 'inicio.html')


#Vistas para proveedor, crear, listar y actualizar, la funcion para eliminar no esta presente
@login_required
def crearProveedor(request):
    if request.method == 'GET':
        return render(request, 'proveedor/form_proveedor.html',{
            'form': ProveedorForm()
        })
    else:
        
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "El proveedor fue guardo con éxito")
            return redirect(reverse('compra:listar_proveedores'))
        
        return render(request, 'proveedor/form_proveedor.html',{
            'form': form,
            'error': 'Por favor, proporcione datos válidos'
        })

@login_required
def listar_proveedor(request):
    provedores = Proveedor.objects.all()
    mensaje = "No hay proveedores disponibles en este momento.\n" + \
              "Necesitas crear nuevos proveedores. Haz click en el icono de la pantalla para comenzar a cargar tus proveedores."
    if not provedores:
        return render(request, 'proveedor/listar_proveedores.html',{'mensaje':mensaje})
    
    return render(request, 'proveedor/listar_proveedores.html', {
        "proveedores": provedores
    })

@login_required
def detalle_proveedor(request, id:int ):
    proveedor = get_object_or_404(Proveedor, id=id)

    
    return render(request, 'proveedor/detalle_proveedor.html',{
        'proveedor': proveedor
    })

@login_required
def modificar_proveedor(request, id):
    if request.method == 'GET':
        proveedor = get_object_or_404(Proveedor, id=id)
        form = ProveedorForm(instance=proveedor)
        return render(request, 'proveedor/modificar_proveedor.html',{
            'proveedor': proveedor,
            'form': form
        })
    else:
        try:
            proveedor = get_object_or_404(Proveedor, id=id)
            form = ProveedorForm(request.POST, instance=proveedor)
            if form.is_valid():
                form.save()  # Guardar el formulario
                messages.success(request, "Actualizado exitosamente")
                return redirect('compra:listar_proveedores')
        except ValueError:
            return render(request, 'proveedor/modificar_proveedor.html',{
            'proveedor': proveedor,
            'form': form,
            'error': "Error al intentar modificar el proveedor."
        })




#Vistas para producto, tenemos crear producto, listar, eliminar, y actializar
@login_required
def crear_producto(request):
    if request.method == 'GET':
        return render(request, 'producto/form_producto.html',{
            'form': ProductoForm()
        })
    else:
        
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,"El producto fue guardado con éxito")
                
            return redirect(reverse('compra:lista_productos'))
        
        return render(request, 'prodcuto/form_producto.html',{
            'form': form,
            'error': 'Por favor, proporcione datos válidos'
        })
    
    
@login_required
def listar_productos(request,):
    productos = Producto.objects.all()
    mensaje = "No hay productos disponibles en este momento.\n" + \
              "Necesitas crear nuevos productos. Haz click en el icono de la pantalla para comenzar a cargar productos."
    if not productos:
        return render(request,'producto/lista_products.html',{'mensaje':mensaje})
    return render(request, 'producto/lista_products.html', {
        'productos':productos 
    })

@login_required
def detalle_producto(request, id:int):
    producto = get_object_or_404(Producto, id=id)
    
    return render(request, 'producto/detalle_producto.html', {
        'producto':producto
    })

@login_required
def modificar_producto(request, id):

    if request.method == 'GET':
        producto = get_object_or_404(Producto, id=id)
        form = ProductoForm(instance=producto)
        return render(request, 'producto/modificar_producto.html',{
            'producto': producto,
            'form': form
        })
    else:
        
        producto = get_object_or_404(Producto, id=id)
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.instance.fecha_de_modificacion = datetime.now()  # Establecer la fecha de modificación en el objeto del formulario
            form.save()  # Guardar el formulario
            messages.success(request, '¡Actualizado exitosamente!')
            return render(request,'producto/detalle_producto.html',{'producto':producto})
       
@login_required
def eliminar_producto(request,id):
    producto = get_object_or_404(Producto, id=id)
    messages.success(request,"El producto fue eliminado correctamente")
    producto.delete()
    return redirect('compra:lista_productos')
    