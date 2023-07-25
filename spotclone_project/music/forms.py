from django import forms
from .models import UserCreatedSong, Playlist

class DeleteSongForm(forms.Form):
    confirm_delete = forms.BooleanField(
        label='Confirm Deletion',
        required=True,
    )
    
class AddSongsToPlaylistForm(forms.ModelForm):
    songs = forms.ModelMultipleChoiceField(
        queryset=UserCreatedSong.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Playlist
        fields = ['songs']


class SongForm(forms.ModelForm):
    class Meta:
        model = UserCreatedSong
        fields = ('image', 'title', 'artist', 'audio_file')
        
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control bg-dark text-light w-50'}), 
            'title': forms.TextInput(attrs={'class': 'form-control bg-dark text-light w-50'}), 
            'artist': forms.TextInput(attrs={'class': 'form-control bg-dark text-light w-50'}), 
            'audio_file': forms.FileInput(attrs={'class': 'form-control bg-dark text-light w-50'}),
        }
    
    def clean_audio_file(self):
        audio_file = self.cleaned_data.get('audio_file')
        if audio_file:
            # Check if the file format is MP3
            if not audio_file.name.endswith('.mp3'):
                raise forms.ValidationError('Only MP3 files are allowed.')
        return audio_file

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('image', 'name', 'description')
        
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control bg-dark text-light w-50'}), 
            'name': forms.TextInput(attrs={'class': 'form-control bg-dark text-light w-50'}), 
            'description': forms.Textarea(attrs={'class': 'form-control bg-dark text-light w-50'}), 
        }