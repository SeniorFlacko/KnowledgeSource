from django.db import models
from modules.users.models import User
from modules.recursos.models import Recurso
# Create your models here.
class Playlist(models.Model):

    user = models.ForeignKey(User)
    nombre = models.CharField(max_length=500)
    playlist_recurso = models.ManyToManyField(Recurso)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.nombre   

