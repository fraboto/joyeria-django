from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    content     = models.TextField()
    author      = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    product     = models.ForeignKey('productos.Product', on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content[:20]
