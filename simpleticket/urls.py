from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('ticket.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


from django.conf import settings

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
			{'document_root': settings.MEDIA_ROOT}),

	)