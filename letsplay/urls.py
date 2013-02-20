from django.conf.urls import patterns, include, url
import letsplay

urlpatterns = patterns('letsplay.views', 
	url(r'$', 'index', name='index'),
)
