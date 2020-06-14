from django.db import models
import uuid as uuid_lib
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.
from ServiceArea.models import ServiceArea
from GasCompany.models import GasCompanyUser


class TankerTruck(models.Model):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    name = models.CharField(max_length=300, null=False, blank=False)
    service_area = models.ForeignKey(ServiceArea, null=True, on_delete=models.SET_NULL,
                                     related_name="service_ares_tanker_truck")
    employee = models.ForeignKey(GasCompanyUser, null=True, on_delete=models.SET_NULL,
                                 related_name="employees_operators_tanker_truck")

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this Tanker Truck should be treated as active. '
            'Unselect this instead of deleting Tanker Trucks.'
        ),
    )

    def __str__(self):
        return f"{self.name} {self.employee} {self.service_area}"

