from django.db import models
from django.utils.translation import gettext as _
from volunteer.models.state import State


class Status(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    key = models.CharField(max_length=200, verbose_name=_("key"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))
    color = models.CharField(blank=True, null=True, max_length=200, verbose_name=_("Color"))
    order = models.PositiveIntegerField(default=1, verbose_name=_("Order"))
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name=_("State"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "وضعیت "
        verbose_name_plural = "وضعیت ها"
