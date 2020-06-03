from django.db import models
from django.contrib.auth.models import User
from community.models import Community
from datetime import datetime

# Create your models here.
class ServicesCategory(models.Model):
    
    service_category = models.CharField(
        max_length=50
    )

    def __str__(self):
        return f"Categoria de serviço: {self.service_category}"

class Services(models.Model):
    """
    Dados de um serviço
    """
    service_title = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )
    service_description = models.TextField(max_length=300)
    service_images = models.ImageField(
        upload_to='img_services', 
        null=True, 
        blank=True
    )
    service_user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    service_category = models.ForeignKey(
        ServicesCategory,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )
    service_community = models.ForeignKey(
        Community,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    service_status = models.CharField(
        max_length=1,
        default='A'
    )
    service_open = models.DateTimeField(
        default=datetime.now
    )
    service_closed = models.DateTimeField(null=True)

    def __str__(self):
        return self.service_title