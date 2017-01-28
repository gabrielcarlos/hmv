from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^teleconsultor/', views.teleconsultor),
    url(r'^solicitante/', views.solicitante),
    url(r'^solicitacao/', views.solicitacao),
]