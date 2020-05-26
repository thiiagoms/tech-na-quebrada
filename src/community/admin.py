from django.contrib import admin
from .models import (
    Community,
    CommunityAddress
)
# Register your models here.
admin.site.register(Community)
admin.site.register(CommunityAddress)