from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio),
    url(r'^puntadas/nueva/$', views.puntada_nueva, name='puntada_nueva'),
    url(r'^lista_puntadas$', views.lista_puntadas, name='lista_puntadas'),
    url(r'^puntadas/new/$', views.puntada_new, name='puntada_new'),
    url(r'^puntadas/(?P<pk>\d+)/remove/$', views.puntadas_remove, name='puntadas_remove'),

    ]
