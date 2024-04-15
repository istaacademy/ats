from django.contrib import admin
from calender.models import (
    Event,
    Time,
)
from django.utils.html import format_html
from jalali_date import date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


class EventAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('interviewer',
                    'interviewee',
                    "status",
                    "show_firm_url",
                    "get_time_jalali",
                    )
    search_fields = ('title',)
    list_editable = ('status',)
    list_filter = ("status", "time",)
    readonly_fields = ("interviewer", "interviewee", "time", "show_firm_url", "title", "link_meeting")

    def get_list_display(self, request):
        # Customize the list_display based on user permissions
        if request.user.is_superuser:
            return self.list_display + ('title', 'description',)
        return self.list_display

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link_meeting)

    show_firm_url.allow_tags = True
    show_firm_url.short_description = 'لینک جلسه'

    @admin.display(description='تاریخ جلسه', ordering='time')
    def get_time_jalali(self, obj):
        date = date2jalali(obj.time.day).strftime('%d %B %Y')
        format_time = '%H:%M:%S'
        return f"{date} time:{obj.time.start_time.strftime(format_time)} to {obj.time.end_time.strftime(format_time)}"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(interviewer=request.user.id)


admin.site.register(Event, EventAdmin)


class TimeAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('get_day_jalali',
                    'start_time',
                    "end_time",
                    "number_reserve"
                    )
    search_fields = ('day',)
    list_filter = ("day",)

    @admin.display(description='تاریخ ', ordering='day')
    def get_day_jalali(self, obj):
        return date2jalali(obj.day).strftime('%d-%B')


admin.site.register(Time, TimeAdmin)
