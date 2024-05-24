from django.contrib import admin
from course.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        "is_active",
    )
    list_filter = ("is_active",)


admin.site.register(Course, CourseAdmin)
