from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso: lectura para todos, escritura sólo para el owner (obj.owner == request.user).
    Si el objeto no tiene 'owner', deniega la escritura.
    """

    def has_object_permission(self, request, view, obj):
        # Métodos seguros: permitir
        if request.method in permissions.SAFE_METHODS:
            return True
        # Comprobar que el objeto tiene atributo owner y coincide con el usuario
        owner = getattr(obj, 'owner', None)
        return owner is not None and owner == request.user