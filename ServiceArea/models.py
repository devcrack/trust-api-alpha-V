from django.db import models
import uuid as uuid_lib
# Create your models here.
from PricesDiscount.models import Price, Discount
from GasCompany.models import GasCompany

class ServiceArea(models.Model):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    gas_company = models.ForeignKey(GasCompany, on_delete=models.CASCADE, null=False, blank=False,
                                    related_name='gas_company_of_service_area')
    name = models.CharField(null=False, max_length=300)
    price = models.OneToOneField(Price, null=True, blank=True, on_delete=models.SET_NULL,
                                 related_name="price_service_area")
    discount = models.OneToOneField(Discount, null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name="discount_service_area")

