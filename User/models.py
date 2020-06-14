from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid as uuid_lib
# Create your models here.
from knox.settings import CONSTANTS, knox_settings

def file_path(instance, filename):
    return '/'.join(['images', str(instance.username), filename])


class User(AbstractUser):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    phone_1 = models.CharField(max_length=16, null=False, unique=True, name='cellNumber1')
    phone_2 = models.CharField(max_length=16, null=True, blank=True, default=None, unique=True, name='cellNumber2')

    REQUIRED_FIELDS = ['first_name', "last_name", 'cellNumber1']

    def __str__(self):
        return f"{self.get_username()}"

class RawToken(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    token = models.CharField(unique=True, null=False, max_length=knox_settings.AUTH_TOKEN_CHARACTER_LENGTH)

    def __str__(self):
        return f"{self.user.get_username()} {self.token}"