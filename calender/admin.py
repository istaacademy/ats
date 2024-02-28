from django.contrib import admin
from calender.models import Event, Time


class EventAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'is_done',
                    "interviewer",
                    "interviewee",
                    "link_meeting",
                    'description',
                    )
    search_fields = ('title',)
    list_editable = ('is_done',)
    list_filter = ("is_done", "interviewee",)

    def get_list_display(self, request):
        # Customize the list_display based on conditions
        if request.user.is_superuser:
            return ('title',
                    'interviewer',
                    'interviewee',
                    'link_meeting',
                    'is_done',
                    'description'
                    )
        else:
            return ('interviewer',
                    'interviewee',
                    'link_meeting',
                    'is_done',
                    'description'
                    )


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
