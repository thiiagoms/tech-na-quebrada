from django.urls import path
from .views import (
   list_community
)
# urls referentes as comunidades
urlpatterns = [
   path('', list_community, name="listcommunity")
]