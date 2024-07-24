from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _
from volunteer.models import Volunteer
import datetime


def user_directory_path(instance, filename):
    date = datetime.datetime.now()
    return 'user_{0}/{1}{2}{3}-{4}'.format(instance.volunteer, date.year, date.strftime("%m"), date.strftime("%d"),
                                           filename)


class TaskTime(models.Model):
    hours = models.PositiveIntegerField(default=0, verbose_name=_("ساعت"))
    days = models.PositiveIntegerField(default=0, verbose_name=_('روز'))


class Task(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name="tasks", verbose_name=_("داوطلب"))
    subject = models.CharField(max_length=300, verbose_name=_("موضوع"), null=True, blank=True)
    send_time = models.DateTimeField(auto_now_add=True, verbose_name=_("زمان ارسال"))
    response_time = models.DateTimeField(null=True, blank=True, verbose_name=_("زمان پاسخ"))
    file = models.FileField(upload_to=user_directory_path, max_length=100, null=True, verbose_name=_("فایل"),
                            validators=[FileExtensionValidator(
                                allowed_extensions=['rar', 'zip', 'pdf', 'JPG', 'JPEG', 'png', 'jpg',
                                                    'jpeg', 'svg', 'SVG', 'xlsx'])])

    @property
    def filename(self):
        return self.file.name

    @property
    def filesize(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x / 1000, 2)
            ext = ' kb'
        elif x < y * 1000:
            value = round(x / 1000000, 2)
            ext = ' Mb'
        else:
            value = round(x / 1000000000, 2)
            ext = ' Gb'
        return str(value) + ext

    @property
    def path(self):
        return self.file

    def __str__(self) -> str:
        return f"{self.volunteer}"

    class Meta:
        verbose_name_plural = "تسک"
        verbose_name = "تسک ها"
