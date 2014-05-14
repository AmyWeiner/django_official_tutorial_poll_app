from django.contrib import admin
from polls.models import Poll

class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['question']}),
    ('Data information', {'fields': ['pub_date']}),
  ]
# Register your models here.
admin.site.register(Poll, PollAdmin)
