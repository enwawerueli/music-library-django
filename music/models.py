from django.db import models
from django.contrib.auth.models import User
from mysite import validators


class Artist(models.Model):

    name = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '"%s"' % self.name


class Album(models.Model):

    title = models.CharField(max_length=255, validators=[validators.string])
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255, validators=[])
    year = models.PositiveIntegerField()

    def upload_to(self, filename):
        path = 'cover/%s_%s/%s_%s.%s'
        extension = filename.split('.')[-1]
        return path % (self.owner.username, self.owner.id, self.title, self.artist.name, extension)

    cover = models.FileField(null=True, blank=True, upload_to=upload_to)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return '"%s" by "%s"' % (self.title, self.artist.name)


class Song(models.Model):

    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, models.CASCADE)

    class Meta:
        ordering = ['album']

    def __str__(self):
        return '"%s" by "%s" from the album "%s"' % (self.title, self.album.title, self.album.artist.name)
