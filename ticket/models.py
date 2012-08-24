from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

TICKET_STATUS_CHOICES = (
		('new', 'New'),
		('accepted', 'Accepted'),
		('assigned', 'Assigned'),
		('reopened', 'Reopened'),
		('closed', 'Closed'),
	)

class Ticket(models.Model):
	assigned_to = models.ForeignKey(User, null=True, blank=True)
	status = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='new')
	description = models.TextField()
	created_on = models.DateTimeField('date created', auto_now_add=True)
	update_on = models.DateTimeField('date updated', auto_now=True)

	def name(self):
		return self.description.split('\n', 1)[0]


class TicketAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_on'
	list_filter = ('status',)
	list_display = ('id', 'name', 'status', 'assigned_to')
	search_fields = ['description']
	
admin.site.register(Ticket, TicketAdmin)