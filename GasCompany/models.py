from django.db import models
import uuid as uuid_lib
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.
from Addresses.models import Address
from User.models import User


class GasCompany(models.Model):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    name = models.CharField(max_length=300, null=False, blank=False)
    creation_date = models.DateTimeField(default=timezone.now)
    address = models.OneToOneField(Address, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="Gas_Station_Address")
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_(
                                        'Designates whether this Gas Company should be treated as active. '
                                        'Unselect this instead of deleting Gas Stations.'
                                    ))

    def __str__(self):
        return f"{self.name} {self.address}"


class GasCompanyUser(models.Model): # La disticion entre Administrador y Administrador la vamos hacer mediante Grupos.
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    user = models.OneToOneField(User, null=False, related_name="User_Admin_GasCompany", on_delete=models.CASCADE)
    gas_company = models.ForeignKey(GasCompany, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.gas_company.name} {self.user}"

