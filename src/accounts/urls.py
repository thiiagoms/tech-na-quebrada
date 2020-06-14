from django.urls import path

from .views import (
    accept_service,
    dashboard,
    profile_user,
    search_user,
    sign_in,
    sign_up,
    update_service_status,
    user_services,
    user_logout,
)
# Urls sobre os voluntarios
urlpatterns = [
    path('accept-service/<int:id>', accept_service, name="acceptservice"),
    path('dashboard', dashboard, name="dashboard"),
    path('login', sign_in, name="sign_in"),
    path('logout', user_logout, name="logout"),
    path('my-services', user_services, name="userservices"),
    path('profile', profile_user, name="userprofile"),
    path('search-volunteers', search_user, name="searchuser"),
    path('sign-up', sign_up, name="sign_up"),
    path('update-service/<int:id>', update_service_status, name="updateservice")
]
