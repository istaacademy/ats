from django.db import models
from django.utils.translation import gettext as _



class State(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name=_("Title"))
    color = models.CharField(blank=True, null=True, max_length=200, verbose_name=_("Color"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    class Meta:
        verbose_name = "موقعیت "
        verbose_name_plural = "موقعیت ها"

    def __str__(self):
        return self.title

