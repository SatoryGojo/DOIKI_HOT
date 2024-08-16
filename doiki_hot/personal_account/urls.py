

from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:pk>', UserCabinet.as_view(), name='your_account'),
    path('delete_from_favorites/<slug:film_slug>', DeleteFavorite, name="delete_favorite")
]