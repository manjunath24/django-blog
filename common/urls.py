from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from common import views

urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       url(r'^about/$',
                           TemplateView.as_view(template_name='about.html'),
                           name='about'),)
