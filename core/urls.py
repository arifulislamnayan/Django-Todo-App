from django.conf.urls import patterns, include, url
from core import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.CreateView.as_view(), name='create'),
)

