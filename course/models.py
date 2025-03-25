from django.db import models
from user.models import User
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class Course(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    registration = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    reservation = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    capacity = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    register_day_start = models.DateField(null=True, blank=True)
    register_day_end = models.DateField(null=True, blank=True,)
    session_number = models.PositiveIntegerField()
    start_time = models.DateField(null=True, blank=True)
    end_time = models.DateField(null=True, blank=True)
    tuition = models.PositiveIntegerField(blank=True, null=True, verbose_name=_("شهریه"))
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    relation = models.CharField(max_length=10, choices=RELATION_CHOISE, default='volunteer')



class TimeCourse(models.Model):
    DAY_OF_THE_WEEK = [
        ('Saturday', "شنبه"),
        ("Sunday", "یکشنبه"),
        ("Monday", "دوشنبه"),
        ("Tuesday", "سه شنبه"),
        ("Wednesday", "چهار شنبه"),
        ("Thursday", "پنجشنبه"),
        ("Friday", "جمعه"),
    ]
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.CharField(max_length=10, choices=DAY_OF_THE_WEEK, default='Thursday')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)