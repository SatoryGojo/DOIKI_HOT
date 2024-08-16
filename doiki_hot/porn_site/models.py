from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Actors(models.Model):
    title = models.CharField(max_length=50, verbose_name='Имя')
    country = models.CharField(max_length=50, verbose_name='Национальность')
    slug = models.SlugField(verbose_name="URL", db_index=True,  unique=True, default="")
    photo = models.ImageField(upload_to='actor_photo', verbose_name='Фотография')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Актеры'
        verbose_name = "Актер"

    def get_absolute_url(self):
        return reverse('actor_films', kwargs={'actor_slug': self.slug})



class Films(models.Model):
    title = models.CharField(max_length=150)
    actor = models.ManyToManyField(Actors, related_name='films')
    studio = models.ManyToManyField('Studio', related_name='studio')
    favourite_video = models.ManyToManyField(User, related_name='favourite_video', blank=True, null=True)
    slug = models.SlugField(verbose_name="URL", blank=True, null=True)
    preview = models.ImageField(upload_to='film_preview')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = "Фильм"


class Studio(models.Model):
    slug = models.SlugField(verbose_name="URL", blank=True, null=True)
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='studio_photo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Студии'
        verbose_name = "Студия"


