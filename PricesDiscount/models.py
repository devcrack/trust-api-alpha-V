from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid as uuid_lib
# Create your models here

class Price(models.Model):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    tax_percentage = models.SmallIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    description = models.CharField(max_length=350, name="Price_Description")


class Discount(models.Model):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    discount_percentage = models.SmallIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    discount_price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=350, name="Discount_Description")


class Credit(models.Model):
    id = models.UUIDField(  # Usado para la busqueda del registro mediante el API
        primary_key=True,
        db_index=True,  # Nunca se deben de usar los ID de la base de datos para hacer busquedas publicas.
        default=uuid_lib.uuid4,
        editable=False)
    limit = models.SmallIntegerField(default=0, validators=[MaxValueValidator(1000000), MinValueValidator(0)])
    term = models.SmallIntegerField(default=0, validators=[MaxValueValidator(1000000), MinValueValidator(0)]) # Plazo
    balance = models.SmallIntegerField(default=0, validators=[MaxValueValidator(1000000), MinValueValidator(0)]) # Saldo




###################
# Good References
###################
""""
https://stackoverflow.com/questions/2013835/django-how-should-i-store-a-money-value
"""

