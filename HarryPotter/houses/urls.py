from django.conf.urls import patterns, include, url

urlpatterns = patterns('houses.views',
	url(r'^$', 'get_houses', {'template_name': 'houses/view.html'}, name='get_houses'),
)
