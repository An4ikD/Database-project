from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('homepage.urls', namespace = 'homepage')),
    url(r'^login/', include('login.urls', namespace = "login")),
    url(r'^enroll/', include('enroll.urls', namespace = "enroll")),
    url(r'^my_profile/', include('my_profile.urls', namespace = 'my_profile')),
    url(r'^students/', include('students.urls', namespace = 'students')),
    url(r'^staff/', include('staff.urls', namespace = 'staff')),
    url(r'^courses/', include('courses.urls', namespace = 'courses')),
    url(r'^houses/', include('houses.urls', namespace = 'houses')),
    url(r'^admin/', include(admin.site.urls)),
)
