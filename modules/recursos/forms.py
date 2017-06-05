from django import forms
from django.forms import ModelForm
from .models import Recurso

class RecursoForm(ModelForm):


    class Meta:
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
        model = Recurso
        fields = ('titulo','lenguaje','tipo','nivel','es_favorito','url')
        widgets = {
            'titulo': forms.TextInput(attrs=
                    {
                        "class": "form-control",
                        "pattern":"^([a-zA-Z]+(?:\.)?(?:(?:'| )[a-zA-Z]+(?:\.)?)*)$",
                    }
                ),
            'lenguaje': forms.Select(attrs={'class': 'form-control'},choices=LENGUAJE_CHOICES),
            'tipo': forms.Select(attrs={'class': 'form-control'},choices=TIPO_CHOICES),
            'nivel': forms.Select(attrs={'class': 'form-control'},choices=NIVEL_CHOICES),
            'es_favorito': forms.NumberInput(attrs=
                    {
                        'class': 'form-control',
                        'value': 0
                    }
                ),
            'url': forms.URLInput(attrs=
                    {
                        'class': 'form-control',
                    }
                ),

        }