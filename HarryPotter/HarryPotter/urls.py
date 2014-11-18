from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('welcome.urls', namespace = 'welcome')),
    url(r'^my_profile/', include('my_profile.urls', namespace = 'my_profile')),
    url(r'^qwerty/$', include('qwerty.urls', namespace = 'qwerty')),
    url(r'^admin/', include(admin.site.urls)),
)
