from datos.models import Preguntas, Respuestas, Usuario
from django.contrib import admin

# Register your models here.
from datos import *

admin.site.register(Preguntas)
admin.site.register(Respuestas)
admin.site.register(Usuario)