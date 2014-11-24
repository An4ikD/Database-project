from django.conf.urls import patterns, include, url

urlpatterns = patterns('login.views',
	url(r'^$', 'sign_in', {'template_name': 'login/view.html', 'redirect_name': '/my_profile/'}, name='sign_in'),
	url(r'^sign_out/$', 'sign_out', {'redirect_name': '/'}, name='sign_out'),
)
urlpatterns += patterns('',
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'welcome/view.html'}),
)
