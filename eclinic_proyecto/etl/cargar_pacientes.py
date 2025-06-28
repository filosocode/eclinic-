import csv
from apps.pacientes.models import Paciente


def cargar_pacientes_desde_csv(ruta_archivo):
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            Paciente.objects.get_or_create(
                nombre=fila['nombre'],
                correo=fila['correo'],
                fecha_nacimiento=fila['fecha_nacimiento']
            )