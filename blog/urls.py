from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.post_list),
		url(r'^valores$', views.valores),
		url(r'^mision$', views.mision),
		url(r'^vision$', views.vision),
		url(r'^registro$', views.registro),
        url(r'^index$', views.index),
        url(r'^indexmanos$', views.indexmanos),
]