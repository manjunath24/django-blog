from django.conf.urls import patterns, include, url

from agiliq_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poll.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home,name='home'),
    url(r'^detail/(?P<blog_id>\d+)/$', views.detail,name='details'),
    url(r'^about/$', views.about,name='about'),
)
