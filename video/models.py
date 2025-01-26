from django.db import models
from django.core.validators import MinValueValidator

class Video(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    time = models.TimeField()
    order = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.size} MB)"

    class Meta:
        ordering = ['created_at']
        verbose_name = "ویدیو"
        verbose_name_plural = "ویدیوها"
