from django.contrib import admin
from course.models import (
    Course ,
    CourseUserModel,
    TimeCourse
     
)

from jalali_date import date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


class TimeCourseInline(admin.TabularInline):  # یا StackedInline برای نمایش عمودی
    model = TimeCourse
    extra = 1  # تعداد فرم‌های خالی پیش‌فرض
    fields = ('start_time', 'end_time', 'day')


@admin.register(Course)
class CourseAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = (
                    'title',
                    "registration",
                    "capacity",
                    "get_time_jalali",
                    "session_number",
                    "created_at",
                    "updated_at",
                    )
    readonly_fields = ("registration", )
    inlines = [TimeCourseInline]


    @admin.display(description='بازه برگزاری دوره', ordering='day')
    def get_time_jalali(self, obj):
        start_date = date2jalali(obj.start_time).strftime('%d %B %Y')
        end_date = date2jalali(obj.end_time).strftime('%d %B %Y')
        return f"{start_date}  to {end_date}"

@admin.register(CourseUserModel)
class CourseUserModelAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'relation', 'created_at')
    raw_id_fields = ("user", 'course')
    list_filter = ('created_at', 'updated_at', 'relation')

