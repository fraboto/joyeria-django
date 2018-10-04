from django.db import models

# Create your models here.
class Bag(models.Model):
    products    = models.ManyToManyField('productos.Product', blank=True)
    price       = models.IntegerField()

    def __str__(self):
        return str(self.price)

class Sell(models.Model):
    bag     = models.OneToOneField('ventas.Bag', on_delete=models.PROTECT)
    user    = models.ForeignKey('usuarios.UDUser', on_delete=models.PROTECT, related_name='sells')

    def __str__(self):
        return self.user.user.username
