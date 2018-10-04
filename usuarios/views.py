from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from .models import UDUser

# Create your views here.
class login_view(LoginView):
    template_name = "usuarios/login.html"

class logout_view(LogoutView):
    next_page = 'login'

def sign_up_view(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user     = authenticate(username=username, password=password)
        login(request, user)
        return redirect('inicio')
    return render(request, 'usuarios/sign_up.html', {'form': form})

class editar_perfil_view(UpdateView):
    model = UDUser
    fields = ['birthday', 'suscribed', 'phone']
    template_name_suffix = '_update_form'
    success_url = "/productos/lista_productos/"
