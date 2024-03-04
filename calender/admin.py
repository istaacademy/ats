from django.contrib import admin
from calender.models import (
    Event,
    Time,
)
from django.utils.html import format_html


class EventAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'status',
                    "interviewer",
                    "interviewee",
                    "link_meeting",
                    'description',
                    )
    search_fields = ('title',)
    list_editable = ('status',)
    list_filter = ("status", "interviewee",)

    def get_list_display(self, request):
        # Customize the list_display based on conditions
        if request.user.is_superuser:
            return ('title',
                    'interviewer',
                    'interviewee',
                    'status',
                    'description',
                    "show_firm_url",
                    )
        else:
            return ('interviewer',
                    'interviewee',
                    'show_firm_url',
                    'status',
                    'description',
                    )

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link_meeting)

    show_firm_url.allow_tags = True
    show_firm_url.short_description = 'link meeting'


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
