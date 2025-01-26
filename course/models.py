from django.db import models
from django.core.validators import MinValueValidator


class Course(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    registration = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    reservation = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    cancel = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    capacity = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    RELATION_CHOISE = [
        ('teacher', 'TEACHER'),
        ('user', 'USER'),
        ('mentor', 'MENTOR'),
    ]
    relation = models.CharField(max_length=10, choices=RELATION_CHOISE, default='user')

    def __str__(self):
        return f"{self.title} (ظرفیت: {self.capacity})"

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره‌ها"
        ordering = ['-created_at']
