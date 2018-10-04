from django.urls import path
from .views import *
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path("agregar_producto/",staff_member_required(agregar_producto_view.as_view()), name="agregar_producto"),
    path("agregar_categoria/", staff_member_required(agregar_categoria_view.as_view()), name="agregar_categoria"),
    path("agregar_material/", staff_member_required(agregar_material_view.as_view()), name="agregar_material"),
    path("", lista_categorias_view.as_view(), name="lista_categorias"),
    path("lista_productos/", lista_productos_view.as_view(), name="lista_productos"),
    path("lista_materiales/", lista_materiales_view.as_view(), name="lista_materiales"),
    path("<slug:slug>/", producto_detail_view.as_view(), name="detalle_producto"),
    path("categoria/<int:pk>/", categoria_detail_view, name="detalle_categoria"),
    path("material/<int:pk>/", material_detail_view, name="detalle_material"),
    path("producto/<int:pk>/", staff_member_required(desactivar_producto_view), name="desactivar_producto"),
    path("actualizar_producto/<slug:slug>/", staff_member_required(product_update_view.as_view()), name="actualizar_producto"),
]
