from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
  puntaje = models.IntegerField(null=True)

  def __str__(self) -> str:
    return f'Usuario {self.id}: {self.username} {self.first_name} {self.last_name} {self.email} {self.is_staff} {self.is_active} {self.puntaje}'
