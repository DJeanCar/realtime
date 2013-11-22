from django.conf.urls import patterns, include, url
from .views import IndexView,LibroView,NuevoComentario

urlpatterns = patterns('',
    
    url(r'^$' , IndexView.as_view()),
    url(r'^libro/$' , LibroView.as_view()),
    url(r'^/nuevo-comentario/$' , 'apps.core.views.NuevoComentario'),
)
