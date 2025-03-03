from django.db import models
from user.models import User
from django.core.validators import MinValueValidator

class Course(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    registration = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    reservation = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    registration_time = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}:{self.capacity})"

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره‌ها"
        ordering = ['-created_at']


class CourseUserModel(models.Model):
    RELATION_CHOISE = [
        ('teacher', 'TEACHER'),
        ('volunteer', 'VOLUNTEER'),
        ('mentor', 'MENTOR'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    relation = models.CharField(max_length=10, choices=RELATION_CHOISE, default='volunteer')

