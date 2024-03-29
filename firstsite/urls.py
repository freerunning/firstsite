from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from polls import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
