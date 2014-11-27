from django.conf.urls import patterns, include, url

urlpatterns = patterns('enroll.views',
    url(r'^$', 'enroll', {'template_name': 'enroll/enroll.html', 'redirect_name': '/enroll/success'}, name='enroll'),
    url(r'^success/$', 'enroll_success', {'template_name': 'enroll/enroll_success.html'}, name='enroll_success'),
)