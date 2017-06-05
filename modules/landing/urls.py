#Urls de app landing
from django.conf.urls import url
from .views import index, login, signup, logout, add_playlist,add_recurso, search
app_name = 'landing'
urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^signup/$', signup,name="sign"),
    url(r'^login/$', login,name="login"),
    url(r'^logout/$', logout,name="logout"),
    url(r'^add_playlist/$', add_playlist,name="add_playlist"),
    url(r'^add_recurso/$', add_recurso,name="add_recurso"),
    url(r'^search/$', search,name="search"),
]
