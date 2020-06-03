from django.shortcuts import (
    HttpResponseRedirect,
    get_object_or_404,
    render,
    redirect,
)
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model
)
from django.contrib.auth.decorators import (
    login_required
)
from django.contrib.auth.models import (
    User
)
from services.models import (
    Services
)

from .forms import (
    VolunteerLoginForm,
    VolunteerRegisterForm,
    VolunteerEditForm
)
from .models import (
    UserProfile
)

# Create your views here.
def sign_up(request):
  
    next = request.GET.get('next')
    form = VolunteerRegisterForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        volunteer = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        avatar = form.cleaned_data.get('image')
        volunteer.set_password(password)
        volunteer.save()
        
        user = User.objects.get(username=username)
        
        userprofile = UserProfile.objects.create(user=user, avatar=avatar)
        
        userprofile.save()
        
        auth_volunteer = authenticate(
            username=volunteer.username,
            password=password
        )
        login(request, auth_volunteer)
        if next:
            return redirect(next)
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, "backend/volunteers/register.html", context)

def sign_in(request):

    next = request.GET.get('next')
    form = VolunteerLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        volunteer = authenticate(
            username=username,
            password=password
        )
        login(request, volunteer)
        # Session objects
        request.session['username'] = username
        if next:
            return redirect(next)
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, "backend/volunteers/login.html", context)
    
@login_required
def dashboard(request):
    current_user = request.user
    user = User.objects.get(pk=current_user.id)
    context = {
        'user_data': user
    }
    return render(request, "backend/volunteers/home.html", context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/volunteer/login')
    
@login_required
def accept_service(request, id):
    service_request = Services.objects.get(pk=id)
    current_user = request.user
    volunteer = User.objects.get(pk=current_user.id)
    service_request.service_status = "O"
    service_request.service_user = volunteer
    service_request.save()
    return redirect('listService')

@login_required
def profile_user(request):
    current_user = request.user
    volunteer = User.objects.get(pk=current_user.id)
    form = VolunteerEditForm(
        request.POST or None,
        request.FILES or None,
        instance=volunteer
    )
    if form.is_valid():
        edit_volunteer = form.save(commit=False)
        password = form.cleaned_data.get('password')
        print(password)
        edit_volunteer.set_password(password)
        edit_volunteer.save()
        new_auth = authenticate(
            username=edit_volunteer.username,
            password=password
        )
        login(request, new_auth)
    context = {
        'form': form
    }
    return render(request, "backend/volunteers/profile.html", context)

@login_required
def user_services(request):
    current_user = request.user
    services = Services.objects.all().filter(
        service_user = current_user.id
    )
    context = {
        'services': services
    }
    return render(request, "backend/volunteers/services.html", context)

@login_required
def update_service_status(request, id):
    services = Services.objects.get(pk=id)
    services.service_status = "C"
    services.save()
    return redirect('userservices')

@login_required
def search_user(request):
    
    search_user = request.GET.get('searchuser' or None)

    if search_user:
        users = User.objects.all().filter(username=search_user)
    else:
        users = User.objects.all()[:3]

    context = {
       'users': users
    }

    return render(request, "backend/volunteers/search.html", context)