from django.contrib import admin
from . models import Choice, Poll, Vote


class ChoiceInline(admin.StackedInline):
    model = Choice


class PollAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline
    ]


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Vote)

