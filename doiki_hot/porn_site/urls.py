
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('categories/', views.CategoriesPage.as_view(), name='categories'),
    path('actors/', views.ActorsPage.as_view(), name='actors'),
    path('actors/<slug:actor_slug>/', views.ActorFilmsPage.as_view(), name='actor_films'),
    path('<slug:film_slug>/', views.FilmDetailHome.as_view(), name='film_view'),
    path('add_to_favorite/<slug:film_slug>', views.AddFavorites, name='add_to_favorite'),
]
