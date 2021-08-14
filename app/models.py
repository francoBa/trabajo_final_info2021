from django.db import models

# Create your models here.
class Pregunta(models.Model):
  '''
    Tabla de Preguntas tiene relación con respuestas y categorías
  '''
  pregunta = models.CharField(max_length=255, null=False, blank=False)
  categoria = models.IntegerField()

  def __str__(self) -> str:
    return f'Pregunta {self.id}: categoría {self.categoria} {self.pregunta}'


class Respuesta(models.Model):
  '''
    Tabla de Respuestas relacionada a la pregunta creada. No puede cargarse sin relación
  '''
  respuesta = models.CharField(max_length=255, null=False, blank=False)
  pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, null=False)
  correcta = models.BooleanField(default=False)

  def __str__(self) -> str:
    return f'Respuesta {self.id}: {self.respuesta} es correcta: {self.correcta}'
