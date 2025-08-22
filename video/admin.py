from django.contrib import admin
from django import forms
from video.models import Video
from video.utils import upload_video  # We'll create this function

class VideoAdminForm(forms.ModelForm):
    file = forms.FileField(required=True)

    class Meta:
        model = Video
        fields = ["title", "file", "course", "duration", "order"]

    def save(self, commit=True):
        file = self.cleaned_data.pop("file", None)
        video = super().save(commit=False)

        if file:
            file_url = upload_video(file, file.name)
            video.file_url = file_url
            video.title = file.name

        if commit:
            video.save()
        return video

class VideoAdmin(admin.ModelAdmin):
    form = VideoAdminForm
    list_display = ("title", "file_url", "course", "duration", "order")
    readonly_fields = ("title", )

admin.site.register(Video, VideoAdmin)