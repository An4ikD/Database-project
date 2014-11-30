from django.conf.urls import patterns, include, url

urlpatterns = patterns('houses.views',
	url(r'^$', 'get_houses', {'template_name': 'houses/view.html'}, name='get_houses'),
	url(r'^add/$', 'add_house', {'template_name': 'houses/add.html', 'redirect_name': '/houses'}, name='add_house'),
	url(r'^delete/(?P<houseName>\w+)', 'delete_house', {'template_name': 'houses/delete.html'}, name='delete_house'),
	url(r'^edit/(?P<houseName>\w+)', 'edit_house', {'template_name': 'houses/edit.html', 'redirect_name': '/houses/'}, name='edit_house'),
)
