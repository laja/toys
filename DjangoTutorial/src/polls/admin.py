from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInLine]
	list_display = ('question', 'pub_date', 'was_published_today')
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hieararchy= 'pub_date'
	
admin.site.register(Poll, PollAdmin)
