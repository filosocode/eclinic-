from django.db import models

# Create your models here.
from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre