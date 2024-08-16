from django.contrib import admin
from course.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'start_date',
        'end_date',
        "is_active",
    )
    list_filter = ("is_active",)


admin.site.register(Course, CourseAdmin)
