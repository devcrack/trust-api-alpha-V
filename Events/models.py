from django.db import models
import uuid as uuid_lib
from django.utils import timezone
# Create your models here.
from Gelocation.models import Geolocation
from TankerTruck.models import TankerTruck


class Event(models.Model):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    date_time = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=300, blank=False, null=False)
    geodata = models.OneToOneField(Geolocation, null=False, blank=False, on_delete=models.CASCADE,
                                   related_name="geodata_event")
    tanker_truck = models.OneToOneField(TankerTruck, null=False, blank=False, on_delete=models.CASCADE,
                                        related_name="tanker_trucks_event")
    raw_data = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.date_time, self.geodata}"



