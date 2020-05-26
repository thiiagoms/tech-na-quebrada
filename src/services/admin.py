from django.contrib import admin
from .models import (
    Services,
    ServicesCategory
)
# Register your models here.
admin.site.register(Services)
admin.site.register(ServicesCategory)
