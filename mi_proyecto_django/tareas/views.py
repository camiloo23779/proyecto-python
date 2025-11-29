from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tarea, Usuario
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ClienteSerializer
from .permissions import IsOwnerOrReadOnly

# -------------------------
# Vistas basadas en clases (HTML/templates) para Tarea (sin cambios funcionales)
# -------------------------
class TareaListView(ListView):
    model = Tarea
    template_name = 'tareas/lista_tareas.html'
    context_object_name = 'tareas'

class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tareas/detalle_tarea.html'
    context_object_name = 'tarea'

class TareaCreateView(CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'estado', 'proyecto']
    template_name = 'tareas/formulario_tarea.html'
    success_url = reverse_lazy('lista_tareas')

class TareaUpdateView(UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'estado', 'proyecto']
    template_name = 'tareas/formulario_tarea.html'
    success_url = reverse_lazy('lista_tareas')

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'tareas/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_tareas')


# -------------------------
# API: ClienteViewSet (para el modelo Usuario, registrado como 'clientes')
# - TokenAuthentication habilitado
# - Permisos: lectura pública; escritura solo owner (IsOwnerOrReadOnly)
# -------------------------
class ClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para 'clientes' (modelo Usuario).
    - GET list/retrieve: abierto (IsAuthenticatedOrReadOnly)
    - POST/PUT/PATCH/DELETE: requiere autenticación y ser owner del objeto
    """
    queryset = Usuario.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Al crear, asignar owner al usuario autenticado (si hay)
        # Nota: owner es opcional en el modelo; si no existe request.user, se guardará null.
        user = getattr(self.request, 'user', None)
        if user and user.is_authenticated:
            serializer.save(owner=user)
        else:
            serializer.save()