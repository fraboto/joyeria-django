from django.urls import path
from .views import *
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('crear_comentario', create_comment, name='crear_comentario'),

]
