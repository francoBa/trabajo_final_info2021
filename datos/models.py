from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
  puntaje = models.IntegerField(null=True)

  def __str__(self) -> str:
    return f'Usuario {self.id}: {self.username} {self.first_name} {self.last_name} {self.email} {self.is_staff} {self.is_active} {self.puntaje}'

class Pregunta(models.Model):
  '''
    Tabla de Preguntas tiene relación con respuestas y nivelación
  '''
  pregunta = models.CharField(max_length=255, null=False, blank=False)
  categoria = models.IntegerField()

  def __str__(self) -> str:
    return f'Pregunta {self.id}: nivel {self.categoria} {self.pregunta}'

class Respuesta(models.Model):
  '''
    Tabla de Respuestas relacionada a la pregunta creada. No puede cargarse sin relación
  '''
  respuesta = models.CharField(max_length=255, null=False, blank=False)
  pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, null=False)

  def __str__(self) -> str:
    return f'Respuesta {self.id}: {self.respuesta}'
