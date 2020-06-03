from django.db import models

# Create your models here.

class CommunityAddress(models.Model):
    """
    Endereços dentro de uma comunidade
    """
    community_address = models.CharField(
        max_length=100
    )
    community_number = models.CharField(
        max_length=100
    )
    
    def __str__(self):
        return f"Endereço: {self.community_address}"

class Community(models.Model):
    """
    Comunidade
    """
    community_name = models.CharField(
        max_length=50
    )
    community_image = models.ImageField(
        upload_to='img_community'
    )
    community_address = models.ForeignKey(
        CommunityAddress,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Comunidade: {self.community_name}"
        
    
