from django.conf.urls import patterns, include, url

urlpatterns = patterns('students.views',
	url(r'^$', 'get_students', {'template_name': 'students/view.html'}, name='get_students'),
	url(r'^dismiss/(?P<id>\w+)', 'dismiss_student', {'template_name': 'students/dismiss.html'}, name='dismiss_student'),
)
