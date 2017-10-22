from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from music.models import Album, Song
from music.forms import AddArtistForm, AddAlbumForm, AddSongForm
from django.http import JsonResponse, HttpResponse


@login_required
def home(request, **kwargs):
    template = 'music/albums.htm'
    return render(request, template)


@login_required
def albums(request, **kwargs):
    template = 'music/albums.htm'
    albums = Album.objects.filter(owner=User.objects.get(id=request.user.id))
    return render(request, template, {'albums': albums})


@login_required
def songs(request, **kwargs):
    template = 'music/songs.htm'
    albums = Album.objects.filter(owner=User.objects.get(id=request.user.id))
    all_songs = []
    for album in albums:
        album_songs = Song.objects.filter(album=album)
        for song in album_songs:
            all_songs.append(song)
    return render(request, template, {'songs': all_songs})


@login_required
def artists(request, **kwargs):
    pass


@login_required
def genres(request, **kwargs):
    pass


@login_required
def favourites(request, **kwargs):
    pass


@login_required
def album_details(request, **kwargs):
    template = 'music/album_details.htm'
    album = Album.objects.get(id=kwargs.get('album'))
    songs = Song.objects.filter(album=album)
    return render(request, template, {'album': album, 'songs': songs})


@login_required
def add_album(request, **kwargs):
    template = 'music/add_album.htm'
    context = None
    if request.method == 'POST':
        form = AddAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.cleaned_data
            album['owner'] = User.objects.get(id=request.user.id)
            added_album = Album.objects.create(**album)
            if added_album:
                messages.success(request, 'Album added successfully.')
            return redirect(reverse('album_detail', kwargs={'album': added_album.id}))
        else:
            context = {'errors': form.errors}
    return render(request, template, context)


@login_required
def add_song(request, **kwargs):
    album = Album.objects.get(id=kwargs.get('album'))
    added_song = Song.objects.create(title=request.POST.get('title'), album=album)
    if added_song:
        messages.success(request, 'Song added successfully.')
        return redirect(reverse('album_detail', kwargs=kwargs))


@login_required
def delete_album(request, **kwargs):
    deletion = Album.objects.get(id=kwargs.get('album')).delete()
    if deletion:
        messages.success(request, 'Album deleted successfully.')
        messages.success(request, 'All songs (%s) from this album were also deleted.' % deletion[1].get('music.Song', 0))
    return redirect(reverse('albums'))


@login_required
def delete_song(request, **kwargs):
    album = Album.objects.get(id=kwargs.get('album'))
    deletion = Song.objects.get(id=kwargs.get('song'), album=album).delete()
    if deletion:
        messages.success(request, 'Song deleted successfully.')
    return redirect(reverse('album_detail', kwargs={'album': kwargs.get('album')}))


def ajax(request, **kwargs):
    if request.is_ajax():
        return JsonResponse({'status': 'ajax '})
    else:
        return HttpResponse('not ajax')
