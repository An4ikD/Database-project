from django.conf.urls import patterns, include, url

urlpatterns = patterns('courses.views',
	url(r'^$', 'get_courses', {'template_name': 'courses/view.html'}, name='get_courses'),
	url(r'^register/(?P<id>\w+)', 'register_course', {'template_name': 'courses/register.html'}, name='register_course'),
	url(r'^drop/(?P<id>\w+)', 'drop_course', {'template_name': 'courses/drop.html'}, name='drop_course'),
	url(r'^add/$', 'add_course', {'template_name': 'courses/add.html', 'redirect_name': '/courses'}, name='add_course'),
	url(r'^delete/(?P<id>\w+)', 'delete_course', {'template_name': 'courses/delete.html'}, name='delete_course'),
	url(r'^edit/(?P<id>\w+)', 'edit_course', {'template_name': 'courses/edit.html', 'redirect_name': '/courses/'}, name='edit_course'),
	url(r'^teach/(?P<id>\w+)', 'teach_course', {'template_name': 'courses/teach.html'}, name='teach_course'),
)
