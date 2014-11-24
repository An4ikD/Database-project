from django.conf.urls import patterns, include, url

urlpatterns = patterns('login.views',
	url(r'^$', 'login', {'template_name': 'login/view.html'}, name='login'),
)
urlpatterns += patterns('',
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'welcome/view.html'}),
)
