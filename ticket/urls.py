from django.conf.urls.defaults import *
from models import Ticket

info = {
	'queryset': Ticket.objects.all(),
}

urlpatterns = patterns('django.views.generic.list_detail',
		url(r'^$', 'object_list', info, name='ticket-list'),
		url(r'^(?P<object_id>\d+)/$', 'object_detail', info, name='ticket-detail'),
	)