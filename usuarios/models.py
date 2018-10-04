from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UDUser(models.Model):
    user        = models.OneToOneField(User, on_delete=models.PROTECT, related_name="usuario")
    birthday    = models.DateField(blank=True, null=True)
    suscribed   = models.BooleanField(default=False)
    phone      	= models.CharField(max_length=15, blank=True, null=True)

    def __str__ (self):
	    return self.user.username
