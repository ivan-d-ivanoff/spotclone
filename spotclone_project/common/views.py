from django.shortcuts import render
from django.views import generic as views
from spotclone_project.music.models import Playlist, UserCreatedSong
# Create your views here.


class HomePageView(views.TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.request.user
        if user.is_authenticated:
            context["playlists"] = Playlist.objects.filter(user=user).order_by('?')[:4]
            context["songs"] = UserCreatedSong.objects.filter(user=user).order_by('?')[:4]
        
        return context
    
    template_name = 'common/home.html'
    