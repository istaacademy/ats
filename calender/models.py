from django.db import models
from accounts.models import User
from volunteer.models import Volunteer
from django.utils.translation import gettext as _


class Time(models.Model):
    day = models.DateField(verbose_name=_('روز'))
    start_time = models.TimeField(verbose_name=_('زمان شروع '))
    end_time = models.TimeField(verbose_name=_('زمان پایان'))
    number_reserve = models.PositiveIntegerField(default=0, verbose_name=_(" تعداد بار رزرو"))

    class Meta:
        verbose_name = "زمان"
        verbose_name_plural = "زمان ها"

    def __str__(self):
        return f"{self.day} time: {self.start_time} to {self.end_time}"


class Event(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'مصاحبه انجام نشده'),
        ('Accept', 'تایید'),
        ('Rejected', 'عدم تایید'),
    ]
    title = models.CharField(max_length=200, verbose_name=_("عنوان"))
    description = models.TextField(blank=True, null=True, max_length=300, verbose_name=_("توضیحات"))
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES[0], max_length=10, verbose_name=_("وضعیت"))
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name="events", verbose_name=_("زمان"))
    interviewer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="interviewer",
                                    verbose_name=_("مصاحبه کننده"))
    interviewee = models.ForeignKey(Volunteer, on_delete=models.PROTECT, related_name="interviewee",
                                    verbose_name=_("مصاحبه شونده"))
    link_meeting = models.CharField(max_length=4000, blank=True, null=True, verbose_name=_("لینک جلسه"))

    class Meta:
        ordering = ("time",)
        verbose_name = "رویداد"
        verbose_name_plural = "رویداد ها"

    def __str__(self):
        return self.title
