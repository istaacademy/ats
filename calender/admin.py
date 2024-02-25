from django.contrib import admin
from calender.models import Event, Time


class EventAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',
                    'is_done',
                    "result",
                    "interviewer",
                    "interviewee"
                    )
    search_fields = ('title',)
    list_filter = ("is_done", "interviewer", "interviewee", "result")


admin.site.register(Event, EventAdmin)


class TimeAdmin(admin.ModelAdmin):
    list_display = ('day',
                    'start_time',
                    "end_time",
                    "number_reserve"
                    )
    search_fields = ('day',)
    list_filter = ("day",)


admin.site.register(Time, TimeAdmin)
