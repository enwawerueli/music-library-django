from django import forms
from music.models import Artist, Album, Song
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re


class AddArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('name', 'bio')


class AddAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title', 'artist', 'genre', 'year', 'cover')


class AddSongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ('title',)
