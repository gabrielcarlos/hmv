from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^teleconsultores/', views.teleconsultores),
    url(r'^solicitantes/', views.solicitantes),
    url(r'^solicitantes/[0-9]', views.solicitantes),
    url(r'^solicitacoes/', views.solicitacoes),
]