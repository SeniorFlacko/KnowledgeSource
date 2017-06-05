from django.db import models
from modules.users.models import User
# Create your models here.
class Recurso(models.Model):
    LENGUAJE_CHOICES = (
        ('Python','Python'),
        ('Java','Java'),
        ('PHP','PHP'),
        ('C++','C++'),
        ('javaScript','javaScript'),
        ('C#','C#'),
        ('Ruby','Ruby'),
    )
    TIPO_CHOICES = (
        ('PDF','PDF'),
        ('Video','Video'),
        ('url','url'),
        ('ebook','ebook'),
    )
    NIVEL_CHOICES = (
        ('Básico','Básico'),
        ('Intermedio','Intermedio'),
        ('Avanzado','Avanzado'),
    )


    user = models.ForeignKey(User)
    titulo = models.CharField(max_length=500)
    lenguaje = models.CharField(max_length=200,choices=LENGUAJE_CHOICES)
    tipo = models.CharField(max_length=200,choices=TIPO_CHOICES)
    nivel = models.CharField(max_length=200,choices=NIVEL_CHOICES)
    es_favorito = models.IntegerField()
    url = models.URLField()
    #archivo = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo   

