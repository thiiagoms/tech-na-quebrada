from django.shortcuts import render
from django.contrib.auth.decorators import (
    login_required
)
from .models import (
    Community
)
# Create your views here.
@login_required
def list_community(request):
    communities = Community.objects.all()
    context = {
        "communities": communities
    }
    return render(request, "backend/community/list.html", context)
