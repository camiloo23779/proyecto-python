from django.core.management.base import BaseCommand
from tareas.models import Usuario, Proyecto, Tarea, Etiqueta
from faker import Faker
from datetime import date, timedelta
import random

fake = Faker('es_ES')

class Command(BaseCommand):
    help = 'Carga datos de ejemplo realistas para la app de gestión de tareas'

    def handle(self, *args, **kwargs):
        # Limpiar datos previos
        Usuario.objects.all().delete()
        Proyecto.objects.all().delete()
        Tarea.objects.all().delete()
        Etiqueta.objects.all().delete()

        # Crear etiquetas base
        etiquetas = [
            Etiqueta.objects.create(nombre="Prioridad Alta", color="rojo"),
            Etiqueta.objects.create(nombre="En Revisión", color="amarillo"),
            Etiqueta.objects.create(nombre="Finalizado", color="verde"),
            Etiqueta.objects.create(nombre="Backend", color="azul"),
            Etiqueta.objects.create(nombre="Frontend", color="violeta"),
        ]

        # Crear usuarios
        usuarios = []
        for _ in range(5):
            usuario = Usuario.objects.create(
                nombre=fake.name(),
                correo=fake.email()
            )
            usuarios.append(usuario)

        # Crear proyectos
        proyectos = []
        for usuario in usuarios:
            for _ in range(random.randint(1, 3)):
                proyecto = Proyecto.objects.create(
                    nombre=fake.catch_phrase(),
                    descripcion=fake.text(max_nb_chars=200),
                    fecha_inicio=fake.date_between(start_date='-60d', end_date='today'),
                    usuario=usuario
                )
                proyectos.append(proyecto)

        # Crear tareas
        estados = ['pendiente', 'progreso', 'completada']
        for proyecto in proyectos:
            for _ in range(random.randint(5, 10)):
                tarea = Tarea.objects.create(
                    titulo=fake.sentence(nb_words=4),
                    descripcion=fake.text(max_nb_chars=100),
                    estado=random.choice(estados),
                    proyecto=proyecto
                )
                # Asignar etiquetas aleatorias
                tarea.etiquetas.add(*random.sample(etiquetas, k=random.randint(1, 3)))

        self.stdout.write(self.style.SUCCESS('Seeder avanzado ejecutado: datos de prueba generados correctamente'))
