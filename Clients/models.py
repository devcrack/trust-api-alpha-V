from django.db import models
import uuid as uuid_lib
# Create your models here.
from User.models import User
from Addresses.models import Address
from Gelocation.models import Geolocation
from ServiceArea.models import ServiceArea
from PricesDiscount.models import Credit


class Client(models.Model):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    user = models.OneToOneField(User,null=False, blank=False, on_delete=models.CASCADE)
    observations = models.CharField(max_length=300, blank=True, null=True, default=None)
    address = models.OneToOneField(Address, null=False, blank=False, on_delete=models.CASCADE,
                                   related_name="address_client")
    geolocation = models.OneToOneField(Geolocation, null=False, blank=False, on_delete=models.CASCADE,
                                       related_name="gelocation_client")
    service_area = models.OneToOneField(ServiceArea, null=False, blank=False, on_delete=models.CASCADE,
                                        related_name="service_area_client")
    credit = models.OneToOneField(Credit, null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="credit_client")
    