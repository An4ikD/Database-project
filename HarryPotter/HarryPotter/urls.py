from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('homepage.urls', namespace = 'homepage')),
    url(r'^login/', include('login.urls', namespace = "login")),
    url(r'^my_profile/', include('my_profile.urls', namespace = 'my_profile')),
    url(r'^admin/', include(admin.site.urls)),
)
