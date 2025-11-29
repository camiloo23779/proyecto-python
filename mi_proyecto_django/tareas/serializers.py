from rest_framework import serializers
from .models import Usuario

class ClienteSerializer(serializers.ModelSerializer):
    # mostrar username/email del owner en la respuesta
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo', 'fecha_registro', 'owner']
        read_only_fields = ['id', 'fecha_registro', 'owner']