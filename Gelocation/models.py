from django.db import models
import uuid as uuid_lib
# Create your models here.


class Geolocation(models.Model):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    lon = models.DecimalField(max_digits=9, decimal_places=7, null=False, blank=False)
    lat = models.DecimalField(max_digits=9, decimal_places=7, null=False, blank=False)

    def __str__(self):
        return f"{self.lon} {self.lat}"