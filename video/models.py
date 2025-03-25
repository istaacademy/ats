from django.db import models
from course.models import Course

class Video(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    time = models.TimeField()
    file_url = models.URLField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.time} MB)"

    class Meta:
        ordering = ['created_at']
        verbose_name = "ویدیو"
        verbose_name_plural = "ویدیوها"
