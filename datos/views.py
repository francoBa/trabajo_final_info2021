from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Usuario


# Create your views here.
def iniciar_sesion(request):
  # siguiente = request.GET.get("next", None)

  # categorias = Categoria.objects.all()
  form = AuthenticationForm()
  if request.method == "POST":
    # siguiente = request.POST.get("next", None)
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
  return render(request, "cuenta/login.html", {
    "form": form,
    # "categorias": categorias,
    # "siguiente": siguiente, 
  })

def nuevo_usuario(request):
  form = UserCreationForm()
  return render(request, 'cuenta/nuevo_usuario.html', {'form': form})
