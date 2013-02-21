from django.conf.urls import patterns, include, url

urlpatterns = patterns('letsplay.views', 
	url(r'^$', 'index', name='index'),
	url(r'^customise/$', 'customise', name='customise'),
)
