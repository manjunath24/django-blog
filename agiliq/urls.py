from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agiliq.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'agiliq_app.views.home', name='home'),
    url(r'^detail/(?P<blog_id>[^/]+)', 'agiliq_app.views.detail', name='details'),
    url(r'^about', 'agiliq_app.views.about', name='about'),
)
