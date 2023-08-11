from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Playlist(models.Model):
    
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE) 
   
    image = models.ImageField(blank=True, 
                              null=True)
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    songs = models.ManyToManyField("UserCreatedSong", 
                                   related_name="playlists", 
                                   blank=True)
                                                              
   

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    # Defines the upload path for the audio file
    # MEDIA_ROOT / user_id / filename
    return f"user_{instance.user.pk}/{filename}"


class UserCreatedSong(models.Model):
    image = models.ImageField(blank=True, 
                              null=True)
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to=user_directory_path, 
                                  blank=True, 
                                  null=True)  
   
   

    def __str__(self):
        return self.title 
 