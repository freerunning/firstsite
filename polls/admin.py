from django.contrib import admin
from polls import models
# Register your models here.

class PollAdmin(admin.ModelAdmin):
	list_display = ('question', 'pub_date')

class ChoiceAdmin(admin.ModelAdmin):
	list_display = ('poll', 'choice_text', 'votes')

admin.site.register(models.Poll, PollAdmin)
admin.site.register(models.Choice, ChoiceAdmin)