from django.db import models

# Create your models here.
from django.conf import settings
from modules.playlists.models import Playlist

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
    playlist = models.ForeignKey(Playlist)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

