from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"code": ("name",)}

class MaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"code": ("name",)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Category, CategoryAdmin)
