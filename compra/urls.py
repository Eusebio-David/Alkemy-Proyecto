from django.urls import path

import usuario.views
from . import views 
import usuario
app_name = 'compra'

urlpatterns = [
    #url para index
    path("", views.index, name='index'),
    #url para proveedores
    path("proveedor/", views.crearProveedor, name='proveedor'),
    path("listar/proveedores/", views.listar_proveedor, name="listar_proveedores"),
    path("detalle/proveedor/<int:id>/", views.detalle_proveedor,name="detalle_proveedor"),
    path("modificar/proveedor/<int:id>", views.modificar_proveedor, name="modificar_proveedor"),

    #url para productos
    path("pruducto/", views.crear_producto, name="producto"),
    path("lista/productos", views.listar_productos, name='lista_productos'),
    path("detalle/producto/<int:id>/", views.detalle_producto, name='detalle_producto'),
    path("modificar/producto/<int:id>", views.modificar_producto, name='modificar_producto'),
    path("eliminar/producto/<int:id>/", views.eliminar_producto, name = 'eliminar_producto'),

    #url para los usuarios
    path("registro/usuario/", usuario.views.crear_usuario, name='registrar_usuario'),
    path("login/usuario", usuario.views.login_view, name='login'),
    path("logout/usuario", usuario.views.logout_view, name='logout'),
    
]