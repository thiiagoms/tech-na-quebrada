from django.shortcuts import (
    render,
    redirect,
    HttpResponse
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
def register_volunteer(request):
    """
    Cadastro dos voluntários, após o cadastro é redirecionado para o dashboard
    """
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

def login_volunteer(request):
    """
    Login volunteer 
    """
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
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, "backend/volunteers/login.html", context)
    
@login_required
def home(request):
    current_user = request.user
    user = User.objects.get(pk=current_user.id)
    context = {
        'user_data': user
    }
    return render(request, "backend/volunteers/home.html", context)

@login_required
def logout_user(request):
    logout(request)
    return redirect("index")
    
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
def my_services(request):
    context = {

    }
    return render(request, "backend/volunteers/services.html", context)
