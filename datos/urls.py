from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path("login", views.iniciar_sesion, name="iniciar_sesion"),
  path("nuevo_usuario", views.nuevo_usuario, name="nuevo_usuario"),
]
