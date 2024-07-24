from django.contrib import admin
from volunteer.models import (
    Volunteer,
    State,
    Status,
    Task
)
from django.utils.html import format_html
from calender.models import Event
from django.db.models import Q
from django import forms


class VolunteerAdminForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VolunteerAdminForm, self).__init__(*args, **kwargs)

        # Customize the choices for the 'status' field based on the volunteer's state
        instance = kwargs.get('instance')
        if instance and instance.state:
            statuses = Status.objects.filter(state=instance.state).order_by('order')
            self.fields['status'].choices = [(status.id, status.name) for status in statuses]


class VolunteerAdmin(admin.ModelAdmin):
    form = VolunteerAdminForm
    list_display = ('first_name', 'last_name', 'email', 'status', 'state', 'show_firm_url',)
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('state',)
    readonly_fields = ('first_name',
                       'last_name',
                       'email',
                       'state',
                       'phone_number',
                       'url_github',
                       'year_of_birth',
                       'url_linkedin',)

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url_linkedin)

    show_firm_url.short_description = 'ادرس لینکدین'

    def get_list_display(self, request):
        # Customize the list_display based on user permissions
        if request.user.is_superuser:
            return self.list_display + ('phone_number', 'is_special')
        return self.list_display

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        group = request.user.groups.all().values_list('name', flat=True)
        event = Event.objects.filter(interviewer=request.user.id).values_list("interviewee", flat=True)
        if event.count() > 0:
            return qs.filter(Q(state__name__in=group) & Q(id=event[0]))
        else:
            return qs.none()


admin.site.register(Volunteer, VolunteerAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'state',
                    'key',
                    'is_active',
                    'color',
                    'order'
                    )
    search_fields = ('name',)


admin.site.register(Status, StatusAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('name',
                    "title",
                    'color',
                    'is_active'
                    )
    search_fields = ('name',)


admin.site.register(State, StateAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('volunteer',
                    'send_time',
                    'response_time',
                    'file',
                    )
    readonly_fields = ('send_time', 'response_time', 'volunteer')


admin.site.register(Task, TaskAdmin)
