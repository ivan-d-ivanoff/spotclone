from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic as views
from spotclone_project.music.models import Playlist, UserCreatedSong
from django.db.models import Q
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

class HomePageView(views.TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.request.user
        if user.is_authenticated:
            context["playlists"] = Playlist.objects.filter(user=user).order_by('?')[:4]
            context["songs"] = UserCreatedSong.objects.filter(user=user).order_by('?')[:4]
            
        return context
    
    template_name = 'common/home.html'
    
class SearchResultView(views.ListView):
    model = User
    template_name = 'common/search_results.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        if search_query:
            return User.objects.filter(
                Q(username__icontains=search_query)
            ).distinct()
        return User.objects.none()
        