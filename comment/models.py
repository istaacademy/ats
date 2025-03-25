from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='comments')  # ارجاع به مدل Course در اپ course
    body = models.TextField(max_length=400)
    reply = models.ForeignKey('self', on_delete=models.CASCADE,
                              related_name='r_comments', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.__class__.__name__}-{self.body[:30]}"


    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
        ordering = ['-created_at']
