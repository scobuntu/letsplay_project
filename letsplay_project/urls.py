from django.conf.urls import patterns, include, url
import letsplay
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', include('letsplay.urls')),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
