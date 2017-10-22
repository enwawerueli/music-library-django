from django.conf.urls import url
from music import views

urlpatterns = [
    url(r'^albums/$', views.albums, name='albums'),
    url(r'^songs/$', views.songs, name='songs'),
    url(r'^artists/$', views.artists, name='artists'),
    url(r'^genres/$', views.genres, name='genres'),
    url(r'^favourites/$', views.favourites, name='favourites'),
    url(r'^albums/add/$', views.add_album, name='add_album'),
    url(r'^albums/(?P<album>\d+)/$', views.album_details, name='album_details'),
    url(r'^albums/(?P<album>\d+)/delete/$', views.delete_album, name='delete_album'),
    url(r'^albums/(?P<album>\d+)/add/$', views.add_song, name='add_song'),
    url(r'^albums/(?P<album>\d+)/delete/(?P<song>\d+)$', views.delete_song, name='delete_song'),
]
