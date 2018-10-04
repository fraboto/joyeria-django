from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    name        = models.CharField(max_length=50)
    photo       = models.ImageField(upload_to="fotos/categorias", null=True)
    code        = models.SlugField()
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("detalle_categoria", kwargs={"pk":self.pk})

    def __str__ (self):
	    return self.name

class Material(models.Model):
    name        = models.CharField(max_length=50)
    fineness    = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(999)])
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    code        = models.SlugField()

    def get_absolute_url(self):
        return reverse("detalle_material", kwargs={"pk":self.pk})

    def __str__ (self):
	    return self.name

class Product(models.Model):
    GENDER_CHOICES = (
            ('dama','Dama'),
			('caballero','Caballero'),
		)

    name        = models.CharField(max_length=200)
    slug        = models.SlugField()
    price       = models.IntegerField()
    gender      = models.CharField(max_length=10, choices=GENDER_CHOICES)
    photo       = models.ImageField(upload_to="fotos/productos")
    stock       = models.IntegerField()
    is_onsale   = models.BooleanField(default=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    materials   = models.ManyToManyField(Material)
    category    = models.ForeignKey('productos.Category', on_delete=models.PROTECT, related_name='products')
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("detalle_producto", kwargs={"slug":self.slug})

    def __str__ (self):
	    return self.name
