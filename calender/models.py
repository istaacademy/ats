from django.db import models
from django.contrib.auth.models import User
from volunteer.models import Volunteer, Status


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
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING,  limit_choices_to={'model': "Event",
                                                                                       "is_active": True})
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name="events")
    interviewer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="interviewer")
    interviewee = models.ForeignKey(Volunteer, on_delete=models.PROTECT, related_name="interviewee")
    link_meeting = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویداد ها"

    def __str__(self):
        return self.title
