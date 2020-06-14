from django.contrib import admin
# Register your models here.
from .models import GasCompany, GasCompanyUser

admin.site.register(GasCompany)
admin.site.register(GasCompanyUser)