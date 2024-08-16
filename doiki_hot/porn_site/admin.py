from django.contrib import admin
from .models import *



class ActorAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'country',  'photo')
    list_display_links = ('title', 'slug')
    search_fields = ('title',)
    list_filter = ('country',)
    prepopulated_fields = {'slug': ('title', )}



class FilmsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'preview')
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Actors, ActorAdmin)
admin.site.register(Films, FilmsAdmin)
admin.site.register(Studio)




