from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^puntadas/nueva/$', views.puntada_nueva, name='puntada_nueva'),
    ]
