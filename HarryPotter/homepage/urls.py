from django.conf.urls import patterns, include, url

urlpatterns = patterns('homepage.views',
	url(r'^$', 'view', {'template_name': 'homepage/view.html'}, name = 'homepage'),
    # url(r'^register/$', 'register', {'template_name': 'welcome/register.html', 'redirect_name': '/register/success'}, name='register'),
    # url(r'^register/success/$', 'register_success', {'template_name': 'welcome/success.html'}, name='register_success'),
    # url(r'^logout/$', 'logout_page', {'redirect_name': '/'}, name='logout'),
)
# urlpatterns += patterns('',
# 	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'welcome/view.html'}),
# )
