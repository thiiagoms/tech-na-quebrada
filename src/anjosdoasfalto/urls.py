from django.contrib import admin
from django.urls import (
    include,
    path
)
from django.conf import settings
from django.conf.urls.static import static

# App imports
from accounts import urls as volunteers_urls
from community import urls as community_urls
from services  import urls as service_urls
#from services.views import (
#    create_service,
#    list_service,
#    profile_service
#)
#
from .views import (
    index
)

# project urls 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('volunteer/', include(volunteers_urls)),
    #path('login', login_volunteer, name="loginVolunteer"),
    #path('logout', logout_user, name="logoutVolunteer"),
    #path('dashboard', dashboard, name="home"),
    path('community', include(community_urls)),
    path('services', include(service_urls))
    #path('services', list_service, name="listService"),
    #path('services/create', create_service, name="createService"),
    #path('services/profile/<int:id>', profile_service, name="profileService"),
    #path('volunteer/register', register_volunteer, name="registerVolunteer"),
    #path('volunteer/accept-service/<int:id>', accept_service, name="acceptService"),
    #path('volunteer/profile/', profile_user, name="profileVolunteer"),
    #path('volunteer/my-services', my_services, name="volunteerService")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 