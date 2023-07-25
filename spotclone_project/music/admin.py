from django.contrib import admin
from .models import UserCreatedSong, Playlist

# Register your models here.
@admin.register(UserCreatedSong)
class UserCreatedSongAdmin(admin.ModelAdmin):
    fields = ('title', 'artist', 'image', 'user')
    list_display=('title', 'artist', 'user')
    ordering = ('title', )
    list_filter = ('title', 'artist')
    search_fields = ('title', 'artist', 'user')


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'image', 'songs')
    list_display=('name', 'description', 'image', 'created_at')
    ordering = ('name', )
    list_filter = ('name',)
    search_fields = ('name', 'description')