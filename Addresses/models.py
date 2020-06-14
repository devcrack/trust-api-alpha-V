from django.db import models
import uuid as uuid_lib
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Address(models.Model):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    street = models.CharField(null=False, blank=False, max_length=300)
    neighborhood = models.CharField(null=False, blank=False, max_length=300) # Colonia
    inner_number = models.SmallIntegerField(default=0, validators=[MaxValueValidator(10000), MinValueValidator(0)]) # Numero Interior
    outer_number = models.SmallIntegerField(default=0, validators=[MaxValueValidator(10000), MinValueValidator(0)])
    city = models.CharField(null=False, blank=False, max_length=300)
    state = models.CharField(null=False, blank=False, max_length=300)
    municipality = models.CharField(null=False, blank=False, max_length=300)
    postal_code = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return f"C.P {self.postal_code} {self.street} {self.outer_number}"




