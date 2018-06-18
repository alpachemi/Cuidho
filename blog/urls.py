from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.indexmanos),
		url(r'^thanks/$', views.thanks),
        url(r'^indexeng/$', views.indexeng),
]