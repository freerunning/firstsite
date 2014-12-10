from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^e301/YoudaoDict.exe/$', views.error301, name='error301'),
    url(r'^e302/YoudaoDict.exe/$', views.error302, name='error302'),
    url(r'^e303/YoudaoDict.exe/$', views.error303, name='error303'),
    url(r'^error/(?P<idx>\d+)/$', views.error, name='error'),
    url(r'^time/$', views.current_datetime, name='current_datetime'),
    url(r'^test/$', views.test, name='test'),
    url(r'^test_template/$', views.test_template, name='test_template'),
    url(r'^meta/$', views.display_meta, name='display_meta'),
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^.*$', views.error404, name='error404'),
)
