from django.db import models
from django.conf import settings

# Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    # Owner: referencia al usuario de autenticación de Django
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='clientes'
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']


#  Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='proyectos')

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-fecha_inicio']


#  Tarea
class Tarea(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('progreso', 'En progreso'),
        ('completada', 'Completada'),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_creacion']


#  Etiqueta
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    tareas = models.ManyToManyField(Tarea, related_name='etiquetas', blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Etiquetas'