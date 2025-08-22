from django.db import models
from course.models import Course

class Video(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    duration = models.DurationField(help_text="Video duration in HH:MM:SS format", blank=True, null=True)
    file_url = models.URLField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"


    class Meta:
        ordering = ['-created_at', "order"]
        verbose_name = "ویدیو"
        verbose_name_plural = "ویدیوها"
