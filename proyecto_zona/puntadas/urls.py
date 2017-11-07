from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio),
    url(r'^puntadas/nueva/$', views.puntada_nueva, name='puntada_nueva'),
    ]
