from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from comentarios.forms import *

from .models import *
# Create your views here.

class lista_productos_view(ListView):
    model       = Product
    queryset    = Product.objects.filter(is_onsale=True)

class lista_categorias_view(ListView):
    model       = Category

class lista_materiales_view(ListView):
    model       = Material

class producto_detail_view(DetailView):
    model       = Product

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context

def categoria_detail_view(request, pk):
    objs = Product.objects.filter(category=pk)
    return render(request, 'productos/category_detail.html', locals())

def material_detail_view(request, pk):
    mat = Material.objects.get(pk=pk)
    objs = Product.objects.filter(materials=pk)
    return render(request, 'productos/material_detail.html', locals())

class agregar_producto_view(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy("lista_productos")

class agregar_categoria_view(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('lista_categorias')

class agregar_material_view(CreateView):
    model = Material
    fields = '__all__'
    success_url = reverse_lazy('lista_materiales')

def desactivar_producto_view(request, pk):
    obj = Product.objects.get(pk=pk)
    obj.is_onsale = False
    obj.save()
    return redirect("/productos/lista_productos/")

class product_update_view(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'
