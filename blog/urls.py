from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.indexmanos),
		url(r'^thanks/$', views.thanks),
        url(r'^indexeng/$', views.indexeng),
        url(r'^indexfr/$', views.indexfr),
        url(r'^trabaja/$', views.trabaja),
        url(r'^blog/$', views.bloga),
        url(r'^posta/(?P<postid>\d+)/$', views.posta, name ='postid'),
        url(r'^about/$', views.about),
]