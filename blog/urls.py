from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.indexmanos),
		url(r'^ofertas$', views.ofertas),
		url(r'^mision$', views.mision),
		url(r'^vision$', views.vision),
		url(r'^registro$', views.registro),
        url(r'^index$', views.index),
        url(r'^indexmanos$', views.indexmanos),
]