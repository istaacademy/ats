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
                    'interviewee_url_linkedin',
                    'interviewee_year_of_birth',
                    "show_firm_url",
                    "get_time_jalali",
                    )
    search_fields = ('interviewer',)
    list_editable = ('status',)
    list_filter = ("status", "time",)
    readonly_fields = ("interviewer", "interviewee", "time", "show_firm_url", "title", "link_meeting",
                       'interviewee_url_linkedin', 'interviewee_year_of_birth')

    def get_list_display(self, request):
        # Customize the list_display based on user permissions
        if request.user.is_superuser:
            return self.list_display + ('description',)
        return self.list_display

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link_meeting)

    show_firm_url.allow_tags = True
    show_firm_url.short_description = 'لینک جلسه'

    def interviewee_url_linkedin(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.interviewee.url_linkedin)
    interviewee_url_linkedin.short_description = ' لینکدین داوطلب'

    def interviewee_year_of_birth(self, obj):
        return obj.interviewee.year_of_birth if obj.interviewee else ''
    interviewee_year_of_birth.short_description = ' سال تولد داوطلب'

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
