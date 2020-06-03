from django import forms
from community.models import (
    Community
)
from .models import (
    Services,
    ServicesCategory
)

class ServiceRegisterForm(forms.ModelForm):
    """
    Register Service
    """
    service_title = forms.CharField(
        label="Título do serviço:",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Informe o título do serviço'
            }
        )
    )
    service_category = forms.ModelChoiceField(
        label='Categoria do serviço: ',
        queryset=ServicesCategory.objects.all().order_by('service_category'),
        initial=0
    )
    service_community = forms.ModelChoiceField(
        label="Comunidade escolhida",
        queryset=Community.objects.all().order_by('community_name'),
        initial=0
    )
    service_description = forms.CharField(
        label="Descrição do serviço:",
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Descrição do serviço -Máximo de 300 caracteres'
            }
        )
    )
    service_image = forms.ImageField(
        label="Deseja anexar algumas fotos ?"
    )
    
    class Meta:
        model = Services
        fields = [
            'service_title',
            'service_category',
            'service_description',
            'service_community',
            'service_image'
        ]

    
class ServiceReadyOnly(forms.ModelForm):
    """
    Register Service
    """
    service_title = forms.CharField(
        label="Título do serviço: "
    )
    service_description = forms.CharField(
        label="Descrição do serviço: "
    )
    service_category = forms.ModelChoiceField(
        label="Categoria do serviço: ",
        queryset=ServicesCategory.objects.all()
    )
    service_community = forms.ModelChoiceField(
        label="Comunidade referente: ",
        queryset=Community.objects.all()
    )
    
    def __init__(self, *args, **kwargs):
        super(ServiceReadyOnly, self).__init__(*args, **kwargs)                       
        self.fields['service_title'].disabled=True
        self.fields['service_description'].disabled=True
        self.fields['service_category'].disabled=True
        self.fields['service_community'].disabled=True
    
    class Meta:
        model = Services
        fields = [
            'service_title',
            'service_description',
            'service_category',
            'service_community',
        ]
   
