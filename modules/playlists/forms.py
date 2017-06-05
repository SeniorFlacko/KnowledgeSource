from django import forms
from django.forms import ModelForm
from .models import Playlist

class PlaylistForm(ModelForm):


    class Meta:
        model = Playlist
        fields = ('nombre','playlist_recurso')
        widgets = {

            'nombre': forms.TextInput(attrs=
                    {
                        "class": "form-control",
                        "pattern":"^([a-zA-Z]+(?:\.)?(?:(?:'| )[a-zA-Z]+(?:\.)?)*)$",
                    }
                ),
            'playlist_recurso': forms.SelectMultiple(attrs={'class': 'form-control'}),
            
        }