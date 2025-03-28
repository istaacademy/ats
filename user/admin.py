from django.contrib import admin
from user.models import User,Profile
from django.utils.html import format_html

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
                    "username",
                    "phone_number",
                    "is_active",

                    )
    search_fields = ('username',)
    list_filter = ("is_active", "is_superuser", "is_staff")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
                    "user",
                    'first_name',
                    "last_name",
                    "show_firm_url_github",
                    "show_firm_url",
                    "telephone",
                    "updated_at"
                    )
    search_fields = ('first_name', "last_name")
    list_filter = ("role",)

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url_linkedin)

    show_firm_url.short_description = 'ادرس لینکدین'

    def show_firm_url_github(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url_github)

    show_firm_url_github.short_description = 'ادرس گیت هاب'