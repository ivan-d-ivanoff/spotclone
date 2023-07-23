from django.urls import path, include
from . import views

urlpatterns = (
    path('playlists/', views.PlaylistListView.as_view(), name='playlist_list'),
    path('playlist/create/', views.PlaylistCreateView.as_view(), name='playlist_create'),
    path('playlist/<int:pk>/', views.PlaylistDetailView.as_view(), name='playlist_details'),
    path('playlist/<int:pk>/update/', views.PlaylistUpdateView.as_view(), name='playlist_update'),
    path('playlist/<int:pk>/delete/', views.PlaylistDeleteView.as_view(), name='playlist_delete'),
    
    path('playlist/custom-playlist/', views.CustomSongsListView.as_view(), name='custom_songs_list'),
    
    path('song/add/', views.SongCreateView.as_view(), name='song_add'),
    path('song/<int:pk>/', views.SongDetailsView.as_view(), name='song_details'),
    path('song/<int:pk>/update/', views.SongUpdateView.as_view(), name='song_update'),
    path('song/<int:pk>/delete/', views.SongDeleteView.as_view(), name='song_delete'),
)