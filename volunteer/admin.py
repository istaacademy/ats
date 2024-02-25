from django.contrib import admin
from .models import Volunteer, State, Status
from django.utils.html import format_html


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'email',
                    "phone_number",
                    "status",
                    "state",
                    "show_firm_url"
                    )
    search_fields = ('first_name',)
    list_filter = ("status", "state",)

    # readonly_fields = ("last_name", "first_name", "state", "year_of_birth", "email", "url_linkedin", "phone_number")
    list_editable = ("status",)

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url_linkedin)

    show_firm_url.allow_tags = True
    show_firm_url.short_description = 'Linkedin'


#

admin.site.register(Volunteer, VolunteerAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'color',
                    )
    search_fields = ('name',)


admin.site.register(Status, StatusAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'color',
                    )
    search_fields = ('name',)


admin.site.register(State, StateAdmin)
