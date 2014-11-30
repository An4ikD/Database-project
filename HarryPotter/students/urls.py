from django.conf.urls import patterns, include, url

urlpatterns = patterns('students.views',
	url(r'^$', 'get_students', {'template_name': 'students/view.html'}, name='get_students'),
)
