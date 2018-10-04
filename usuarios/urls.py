from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("login/", login_view.as_view(), name="login"),
    path("logout/", logout_view.as_view(), name="logout"),
    path("signup/", sign_up_view, name="sign_up"),
    path("editar_perfil/<int:pk>/", login_required(editar_perfil_view.as_view()), name="editar_perfil"),
]
