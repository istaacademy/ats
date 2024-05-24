from django.contrib.auth.models import AbstractUser
from django.db import models
from course.models import Course


class User(AbstractUser):
    course = models.ManyToManyField(Course, blank=True)
