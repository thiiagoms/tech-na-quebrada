from django.urls import path
from .views import (
   create_service,
   list_service,
   profile_service,
   search_service
)

# urls referentes as comunidades
urlpatterns = [
  path('', list_service, name="listservice"),
  path('create-service', create_service, name="createservice"),
  path('search-service', search_service, name="searchservice"),
  path('profile-service/<int:id>', profile_service, name="profileservice"),
]