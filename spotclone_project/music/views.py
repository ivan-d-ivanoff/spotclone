from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic as views
from .models import Playlist, UserCreatedSong
from .forms import DeleteSongForm
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

class PlaylistCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Playlist
    fields = ['image', 'name', 'description']
    template_name = 'music/playlist_create.html'
    success_url = reverse_lazy('user_details')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlaylistUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Playlist
    fields = ['image', 'name', 'description']
    template_name = 'music/playlist_update.html'
    success_url = reverse_lazy('user_details')

class PlaylistDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Playlist
    context_object_name = 'playlist'
    template_name = "music/playlist_delete.html"
    success_url = reverse_lazy('user_details')



class SongCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = UserCreatedSong
    fields = ['image', 'title', 'artist', 'audio_file']
    template_name = 'music/song_add.html'
    success_url = reverse_lazy('user_details')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SongUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = UserCreatedSong
    fields = ['image', 'title', 'artist', 'audio_file']
    template_name = 'music/song_update.html'
    success_url = reverse_lazy('user_details')
    context_object_name = 'song'
    
class SongDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = UserCreatedSong
    context_object_name = 'song'
    template_name = "music/song_delete.html"
    success_url = reverse_lazy('user_details')
    
class SongDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = UserCreatedSong
    context_object_name = 'song'
    template_name = 'music/song_details.html'

class CustomSongsListView(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'music/songs_list.html'
    context_object_name = 'custom_songs'
    paginate_by = 36
    
    def get_queryset(self):
        user_pk = self.request.user.pk
        return UserCreatedSong.objects.filter(user_id=user_pk)