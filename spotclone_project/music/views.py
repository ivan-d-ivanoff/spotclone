from typing import Any, Dict
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic as views
from .models import Playlist, UserCreatedSong
from .forms import AddSongsToPlaylistForm, DeleteSongForm, PlaylistForm, SongForm
from spotclone_project.user.models import Profile
from django.contrib.auth import mixins as auth_mixins

class PlaylistListView(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'music/playlist_list.html'
    model = Playlist
    
    context_object_name = 'playlists'
    paginate_by = 12

    
class PlaylistDetailView(auth_mixins.LoginRequiredMixin, views.DetailView):
    pass
    model = Playlist
    template_name = 'music/playlist_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playlist = context['playlist']
        songs = playlist.songs.all()

        context['songs'] = songs
        return context

class PlaylistCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Playlist
    template_name = 'music/playlist_create.html'
    form_class = PlaylistForm
    
    def get_success_url(self):
        return reverse_lazy('user_details', kwargs={'pk': self.request.user.pk})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlaylistUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'music/playlist_update.html'
    
    def get_success_url(self):
        return reverse_lazy('user_details', kwargs={'pk': self.request.user.pk})

class PlaylistDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Playlist
    context_object_name = 'playlist'
    template_name = "music/playlist_delete.html"
    
    def get_success_url(self):
        return reverse_lazy('user_details', kwargs={'pk': self.request.user.pk})
    
    

class SongCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = UserCreatedSong
    template_name = 'music/song_add.html'
    form_class = SongForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('user_details', kwargs={'pk': self.request.user.pk})

class SongUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = UserCreatedSong
    form_class = SongForm
    template_name = 'music/song_update.html'
    context_object_name = 'song'
    
    def get_success_url(self):
        return reverse_lazy('user_details', kwargs={'pk': self.request.user.pk})
    
class SongDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = UserCreatedSong
    context_object_name = 'song'
    template_name = "music/song_delete.html"
    
    def get_success_url(self):
        return reverse_lazy('user_details', kwargs={'pk': self.request.user.pk})
    
class SongDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = UserCreatedSong
    context_object_name = 'song'
    template_name = 'music/song_details.html'

class CustomSongsListView(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'music/songs_list.html'
    context_object_name = 'custom_songs'
    paginate_by = 16
    
    def get_queryset(self):
        user_pk = self.request.user.pk
        return UserCreatedSong.objects.filter(user_id=user_pk)
    

class AddSongToPlaylist(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Playlist
    template_name = "music/add_songs_to_playlist.html"
    success_url = reverse_lazy("home")
    form_class = AddSongsToPlaylistForm
    
    def form_valid(self, form):
        playlist = form.save(commit=False)
        form_songs = form.cleaned_data['songs']
        playlist.songs.add(*form_songs)
        return super().form_valid(form)