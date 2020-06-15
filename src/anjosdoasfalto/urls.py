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

from .views import (
    index
)

# project urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('volunteer/', include(volunteers_urls)),
    path('community/', include(community_urls)),
    path('services/', include(service_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
