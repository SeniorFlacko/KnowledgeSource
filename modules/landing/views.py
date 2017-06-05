from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm
from django.contrib.auth.models import User
from modules.users.models import User
from django.contrib.auth import authenticate,logout as salir,login as iniciar
from django.http import HttpResponse
from modules.playlists.forms import PlaylistForm
from modules.recursos.forms import RecursoForm
from modules.playlists.models import Playlist
from modules.recursos.models import Recurso
# Create your views here.
def index(request):
    form_login = LoginForm(request.POST or None)
    form_sign = SignupForm(request.POST or None)
    form_playlist = PlaylistForm(request.POST or None)
    form_recurso = RecursoForm(request.POST or None)

    usuario = request.user #Obtenemos el usuario que esta actualmente logeado

    if usuario.is_authenticated():
        lista = Playlist.objects.all().select_related().filter(user=usuario) #obtenemos las playlist del usuario 
        lista = lista.exclude(nombre="Favoritos")
        lista = lista.exclude(nombre="Historial")
        favoritos = Playlist.objects.all().select_related().filter(user=usuario,nombre='Favoritos') #obtenemos el playlist 'favoritos' del usuario
        historiales = Playlist.objects.all().select_related().filter(user=usuario,nombre='Historial') #obtenemos las playlist 'Historial' del usuario  
        print(lista) #Revisamos que este devolviendo algo
        return render(request,'landing/index.html',{'login':form_login, 'sign':form_sign,
        'playlist':form_playlist,
        'recurso': form_recurso,
        'playlists': lista, #Mandamos la variable lista con el alias 'playlists' al index
        'favoritos': favoritos, #Mandamos la variable favoritos con el alias 'favoritos' al index
        'historiales': historiales, #Mandamos la variable historial con el alias 'historial' al index
        }
        )

    else:
        return render(request,'landing/index.html',{'login':form_login, 'sign':form_sign,
            'playlist':form_playlist,
            'recurso': form_recurso,
            }
        )


def login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
                )
            if user is not None:
                iniciar(request,user)
                return redirect('landing:index')
            else:
                return redirect('landing:index')#usuario no registrado

    return render(request,'landing/index.html')



def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            form.cleaned_data.pop('confirm_password', None)
            user = User.objects.create_user(**form.cleaned_data)
            if user is not None:
                iniciar(request,user)
                f = Playlist(user=request.user,nombre='Favoritos')
                h = Playlist(user=request.user,nombre='Historial')
                f.save()
                h.save()    
                return redirect("landing:index")
                
    return render(request,'landing/index.html')
            
    


def logout(request):
    salir(request)
    return redirect("landing:index")


def add_playlist(request):
    if request.method == 'POST':
        form_playlist = PlaylistForm(request.POST or None)
        print(form_playlist)
        if form_playlist.is_valid():
            Playlist = form_playlist.save(commit=False)
            u = request.user
            Playlist.user = u
            Playlist.save()
            return redirect('landing:index')
        else:
            return HttpResponse('hola')
    
        

def add_recurso(request):
       if request.method == 'POST':
           form_recurso = RecursoForm(request.POST)
           if form_recurso.is_valid():
                Recurso = form_recurso.save(commit=False)
                u = request.user
                Recurso.user = u
                Recurso.save()
                return redirect('landing:index')

def search(request):
    recuros = None
    if request.method == 'POST':
        recursos = Recurso.objects.filter(titulo__icontains=request.POST['q'])
        print(recursos)
    return render(request,'landing/resultado.html',{'recursos':recursos})