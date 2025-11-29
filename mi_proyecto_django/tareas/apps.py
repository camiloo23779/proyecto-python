from django.apps import AppConfig

class TareasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tareas'

    def ready(self):
        # Importar signals para que se registren (no hacer import en módulo global)
        import tareas.signals  # noqa