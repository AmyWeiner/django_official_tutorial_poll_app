from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.StackedInline):
  model = Choice
  extra = 3

class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['question']}),
    ('Data information', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]
  inlines = [ChoiceInline]
# Register your models here.
admin.site.register(Poll, PollAdmin)
