from django.db import models
import uuid as uuid_lib
from django.utils import timezone
# Create your models here.
from TankerTruck.models import TankerTruck
from Clients.models import Client
from Gelocation.models import Geolocation
from TankerTruck.models import TankerTruck


class Order(models.Model):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    place_reference = models.CharField(max_length=300, blank=True, null=True)
    commitment_date = models.DateTimeField(null=False, blank=False)
    tanker_truck = models.OneToOneField(TankerTruck, null=True, blank=False, on_delete=models.SET_NULL,
                                        related_name="tanker_trucks_orders")
    client = models.OneToOneField(Client, null=False, blank=False, on_delete=models.CASCADE,
                                  related_name="client_order")
    folio = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self):
        return f"{self.commitment_date} {self.tanker_truck} {self.client}"


class Service(models.Model):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    folio = models.CharField(max_length=300, blank=False, null=False)
    volumen = models.IntegerField(default=-1)
    date_time_start = models.DateTimeField(default=timezone.now)
    date_time_end = models.DateTimeField(default=None) #SE PONE COMO null por default por si se quiere posteriormente modifcar este valor
    density = models.DecimalField(max_digits=7, decimal_places=3, default=None)
    mass = models.DecimalField(max_digits=7, decimal_places=3, default=None)
    temperature = models.DecimalField(max_digits=4, decimal_places=3, default=None)
    totalizer_volume = models.IntegerField(default=-1)
    amount_purchase = models.DecimalField(max_digits=7, decimal_places=2)
    geodata = models.OneToOneField(Geolocation, on_delete=models.SET_NULL, default=None, null=True,
                                   related_name="geodata_service")
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=False,
                                 related_name="order_service")
    tanker_truck = models.OneToOneField(TankerTruck, on_delete=models.SET_NULL, null=True,
                                        related_name="tanker_truck_service")

    def __str__(self):
        return f"Folio: {self.folio} {self.date_time_end}"







