from django.db import models

# Create your models here.
class Usuario(models.Model):
  nombre = models.CharField(max_length=50, null=False, blank=False)
  apellido = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  puntaje = models.IntegerField()
  fecha_ult_acceso = models.DateField(auto_now_add=True)
  estado = models.IntegerField()

  def __str__(self) -> str:
    return f'Usuario {self.id}: {self.nombre} {self.apellido} {self.email} {self.puntaje}'

class Preguntas(models.Model):
  '''
    Tabla de Preguntas tiene relación con respuestas y nivelación
  '''
  pregunta = models.CharField(max_length=255, null=False, blank=False)
  nivel = models.IntegerField()

  def __str__(self) -> str:
    return f'Pregunta {self.id}: nivel {self.nivel} {self.pregunta}'

class Respuestas(models.Model):
  '''
    Tabla de respuestas relacionada a la pregunta creada. No puede cargarse sin relación
  '''
  respuesta = models.CharField(max_length=255, null=False, blank=False)
  pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE, null=False)

  def __str__(self) -> str:
    # return f'Respuesta {self.id}: {self.respuesta} {self.pregunta}'
    return f'Respuesta {self.id}: {self.respuesta}'
