from django.conf.urls import patterns, include, url

urlpatterns = patterns('courses.views',
	url(r'^$', 'get_courses', {'template_name': 'courses/view.html'}, name='get_courses'),
	url(r'^register/(?P<id>\w+)', 'register_course', {'template_name': 'courses/register.html'}, name='register_course'),
	url(r'^drop/(?P<id>\w+)', 'drop_course', {'template_name': 'courses/drop.html'}, name='drop_course'),
)
