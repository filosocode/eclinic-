from django.db import models

# Create your models here.
from django.db import models
from apps.pacientes.models import Paciente

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    fecha_hora = models.DateTimeField()
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"Cita de {self.paciente.nombre} el {self.fecha_hora.strftime('%Y-%m-%d %H:%M')}"