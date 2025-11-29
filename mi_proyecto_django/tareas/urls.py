from django.urls import path
from .views import (
    TareaListView,
    TareaDetailView,
    TareaCreateView,
    TareaUpdateView,
    TareaDeleteView
)

urlpatterns = [
    path('', TareaListView.as_view(), name='lista_tareas'),
    path('tarea/<int:pk>/', TareaDetailView.as_view(), name='detalle_tarea'),
    path('tarea/nueva/', TareaCreateView.as_view(), name='crear_tarea'),
    path('tarea/<int:pk>/editar/', TareaUpdateView.as_view(), name='editar_tarea'),
    path('tarea/<int:pk>/eliminar/', TareaDeleteView.as_view(), name='eliminar_tarea'),
]
