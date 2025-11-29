from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as drf_authtoken_views
from tareas.views import ClienteViewSet

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')

urlpatterns = [
    # Incluir las URLs de la app 'tareas' en la raíz para que los nombres de ruta estén disponibles
    path('', include('tareas.urls')),

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Endpoint para obtener token: POST {username, password} -> {token}
    path('api-token-auth/', drf_authtoken_views.obtain_auth_token, name='api_token_auth'),
    # django-allauth
    path('accounts/', include('allauth.urls')),
]