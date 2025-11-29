from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Crea un Token automáticamente cuando se crea un usuario.
    Esto facilita que usuarios autenticados por allauth (incluyendo social login)
    puedan usar TokenAuthentication en la API.
    """
    if created:
        Token.objects.create(user=instance)