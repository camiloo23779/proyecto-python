from django.test import TestCase
from django.urls import reverse
from .models import Usuario, Proyecto, Tarea

class ModeloTareaTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(nombre="Daniel", correo="daniel@example.com")
        self.proyecto = Proyecto.objects.create(
            nombre="Proyecto Test",
            descripcion="Descripción de prueba",
            fecha_inicio="2024-01-01",
            usuario=self.usuario
        )
        self.tarea = Tarea.objects.create(
            titulo="Tarea de prueba",
            descripcion="Descripción de tarea",
            proyecto=self.proyecto
        )

    def test_creacion_tarea(self):
        self.assertEqual(self.tarea.titulo, "Tarea de prueba")
        self.assertEqual(str(self.tarea), "Tarea de prueba")
        self.assertEqual(self.tarea.proyecto.nombre, "Proyecto Test")


class VistasTareaTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(nombre="Daniel", correo="daniel@example.com")
        self.proyecto = Proyecto.objects.create(
            nombre="Proyecto Test",
            descripcion="Descripción de prueba",
            fecha_inicio="2024-01-01",
            usuario=self.usuario
        )
        self.tarea = Tarea.objects.create(
            titulo="Tarea de prueba",
            descripcion="Descripción de tarea",
            proyecto=self.proyecto
        )

    def test_lista_tareas_view(self):
        response = self.client.get(reverse('lista_tareas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tarea de prueba")

    def test_detalle_tarea_view(self):
        response = self.client.get(reverse('detalle_tarea', args=[self.tarea.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tarea.titulo)
