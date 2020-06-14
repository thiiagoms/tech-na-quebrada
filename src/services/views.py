from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404
)
from django.contrib.auth.decorators import login_required
from .forms import (
    ServiceRegisterForm,
    ServiceReadyOnly
)
from .models import (
    Services
)

# Create your views here.
def create_service(request):
    serviceForm = ServiceRegisterForm(request.POST or None, request.FILES or None)
    if serviceForm.is_valid():
        serviceForm.save()
        return redirect('listService')
    context = {
        'form': serviceForm
    }
    return render(request, 'backend/services/register.html', context)

@login_required
def list_service(request):
    services = Services.objects.all()
    context = {
        'services': services
    }
    return render(request, 'backend/services/list.html', context)

@login_required
def profile_service(request, id):
    service = get_object_or_404(Services, pk=id)
    form = ServiceReadyOnly(request.POST or None, instance=service)
    context = {
        'form': form,
        'id': id
    }
    return render(request, 'backend/services/profile.html', context)

@login_required
def search_service(request):
    context = {
    }
    return render(request, "backend/services/search.html", context)