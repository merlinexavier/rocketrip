from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^$', 'activity.views.home', name='home'),
    url(r'^table/$', 'activity.views.table', name='table'),

)
