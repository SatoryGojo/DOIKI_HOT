from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from porn_site.models import Films


class UserCabinet(DetailView):
    model = User
    template_name = 'personal_account/personal_video.html'
    context_object_name = 'user'


def DeleteFavorite(request, film_slug):
    film = Films.objects.get(slug=film_slug)
    film.favourite_video.remove(request.user)
    return redirect('your_account', request.user.id)

