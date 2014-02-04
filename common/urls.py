from django.conf.urls import patterns, include, url

from common import views

urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       url(r'^about/$', views.about, name='about'),)
