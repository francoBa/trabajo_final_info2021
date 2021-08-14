from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.
def iniciar_sesion(request):
  form = AuthenticationForm()
  if request.method == "POST":
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      username = form.cleaned_data["username"]
      password = form.cleaned_data["password"]
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        if user.is_staff:
          return redirect('/admin')
        else:
          return redirect('index')
    else:
      return redirect('nuevo_usuario')
  return render(request, "cuenta/login.html", {"form": form})


def nuevo_usuario(request):
  if request.method == 'POST':
    form = get_user_model()
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = SignUpForm()
  
  return render(request, 'cuenta/nuevo_usuario.html', {'form': form})
