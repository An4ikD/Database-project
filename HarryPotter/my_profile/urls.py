from django.conf.urls import patterns, include, url

urlpatterns = patterns('my_profile.views',
    url(r'^$', 'my_profile', {'template_name': 'my_profile/view.html'}, name='my_profile'),
    url(r'^edit/$', 'edit', {'template_name': 'my_profile/edit.html', 'redirect_name': '/my_profile'}, name='edit'),
    url(r'^logout/$', 'logout_page', {'redirect_name': '/'}, name='logout'),
)
