from django import forms

class DeleteSongForm(forms.Form):
    confirm_delete = forms.BooleanField(
        label='Confirm Deletion',
        required=True,
    )