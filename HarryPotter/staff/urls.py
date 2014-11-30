from django.conf.urls import patterns, include, url

urlpatterns = patterns('staff.views',
	url(r'^$', 'get_staff', {'template_name': 'staff/view.html'}, name='get_staff'),
	url(r'^dismiss/(?P<id>\w+)', 'dismiss_staff', {'template_name': 'staff/dismiss.html'}, name='dismiss_staff'),
)
