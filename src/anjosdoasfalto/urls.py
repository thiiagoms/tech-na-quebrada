from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


# App imports
from accounts.views import (
    register_volunteer, 
    login_volunteer,
    logout_user,
    home,
    accept_service,
    profile_user
)
from services.views import (
    create_service,
    list_service,
    profile_service
)
from community.views import (
    list_community
)
from .views import (
    index
)

# project urls 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('login', login_volunteer, name="loginVolunteer"),
    path('logout', logout_user, name="logoutVolunteer"),
    path('dashboard', home, name="home"),
    path('community', list_community, name="listCommunity"),
    path('services', list_service, name="listService"),
    path('services/create', create_service, name="createService"),
    path('services/profile/<int:id>', profile_service, name="profileService"),
    path('volunteer/register', register_volunteer, name="registerVolunteer"),
    path('volunteer/accept-service/<int:id>', accept_service, name="acceptService"),
    path('volunteer/profile/', profile_user, name="profileVolunteer")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 