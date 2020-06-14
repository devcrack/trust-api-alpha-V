from django.contrib import admin
from .models import User, RawToken
# Register your models here.
admin.site.register(User)
admin.site.register(RawToken)

