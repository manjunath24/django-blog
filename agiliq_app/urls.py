from django.conf.urls import patterns, include, url

from agiliq_app import views

urlpatterns = patterns('',
    url(r'^detail/(?P<blog_id>\d+)/$', views.detail,name='details'),
)
