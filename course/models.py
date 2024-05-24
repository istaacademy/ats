from django.db import models
from django.utils.translation import gettext as _


class Course(models.Model):
    name = models.CharField(max_length=300, verbose_name=_("نام درس"))
    start_date = models.DateTimeField(null=True, blank=True, verbose_name=_("زمان شروع"))
    end_date = models.DateTimeField(null=True, blank=True, verbose_name=_("زمان پایان"))
    is_active = models.BooleanField(default=True, verbose_name=_("فعال"))

    def __str__(self):
        return self.name

