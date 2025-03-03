from django.contrib import admin
from .models import (
    Course ,
     
)

from jalali_date import date2jalali
# from jalali_date.admin import ModelAdminJalaliMixin

class CourseAdmin(admin.ModelAdmin):
    list_display = (
                    'title',
                    "registration",
                    "reservation",
                    "capacity",
                    "created_at",
                    "updated_at"
                    )
    search_fields = ('registration_time',)
    list_filter = ("registration_time",)
    #
    # @admin.display(description='تاریخ ', ordering='day')
    # def get_day_jalali(self, obj):
    #     return date2jalali(obj.registration_time).strftime('%d-%B')



admin.site.register(Course, CourseAdmin)