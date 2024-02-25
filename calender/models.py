from django.db import models
from django.contrib.auth.models import User
from volunteer.models import Volunteer

CHOICES = (
    ("Accepted", "Accepted"),
    ("Rejected", "Rejected"),
    ("Pending", "Pending")
)


class Time(models.Model):
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    number_reserve = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "زمان"
        verbose_name_plural = "زمان ها"

    def __str__(self):
        return str(self.day)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, max_length=300)
    is_done = models.BooleanField(default=False)
    result = models.CharField(choices=CHOICES, max_length=8, default="Pending")
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name="events")
    interviewer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="interviewer")
    interviewee = models.ForeignKey(Volunteer, on_delete=models.PROTECT, related_name="interviewee")

    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویداد ها"

    def __str__(self):
        return self.title
