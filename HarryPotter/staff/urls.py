from django.conf.urls import patterns, include, url

urlpatterns = patterns('staff.views',
	url(r'^$', 'get_staff', {'template_name': 'staff/view.html'}, name='get_staff'),
)
