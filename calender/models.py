from django.db import models
from django.contrib.auth.models import User
from volunteer.models import Volunteer, Status
from django.utils.translation import gettext as _


class Time(models.Model):
    day = models.DateField(verbose_name=_('Day'))
    start_time = models.TimeField(verbose_name=_('Start Time'))
    end_time = models.TimeField(verbose_name=_('End time'))
    number_reserve = models.PositiveIntegerField(default=0, verbose_name="Number of reserves")

    class Meta:
        verbose_name = "زمان"
        verbose_name_plural = "زمان ها"

    def __str__(self):
        return str(self.day)


class Event(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'مصاحبه انجام نشده'),
        ('Accept', 'مصاحبه-پذیرفته شد'),
        ('Rejected', 'مصاحبه - پذیرفته نشد'),
    ]
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = models.TextField(blank=True, null=True, max_length=300, verbose_name=_("Description"))
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES[0], max_length=10)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name="events")
    interviewer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="interviewer",
                                    verbose_name=_("Interviewer"))
    interviewee = models.ForeignKey(Volunteer, on_delete=models.PROTECT, related_name="interviewee",
                                    verbose_name=_("Interviewee"))
    link_meeting = models.CharField(max_length=4000, blank=True, null=True, verbose_name=_("Link meeting"))

    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویداد ها"

    def __str__(self):
        return self.title
