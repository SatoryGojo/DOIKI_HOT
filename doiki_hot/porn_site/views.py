from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Actors, Films



class HomePage(ListView):
    model = Films
    template_name = 'porn_site/home.html'
    context_object_name = 'films'
    paginate_by = 3


class FilmDetailHome(DetailView):
    model = Films
    template_name = 'porn_site/film_page.html'
    context_object_name = 'film'
    slug_url_kwarg = 'film_slug'




class CategoriesPage(TemplateView):
    template_name = "porn_site/categories.html"


class ActorsPage(ListView):
    model = Actors
    template_name = "porn_site/actors.html"
    context_object_name = 'actors'
    paginate_by = 2


class ActorFilmsPage(DetailView):
    model = Actors
    template_name = 'porn_site/actor_films.html'
    context_object_name = 'actor'
    slug_url_kwarg = 'actor_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = context['actor'].title
        return context



def AddFavorites(request, film_slug):
    film = Films.objects.get(slug=film_slug)
    film.favourite_video.add(request.user)
    return redirect('film_view', film_slug)




