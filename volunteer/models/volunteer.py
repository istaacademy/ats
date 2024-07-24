from django.db import models
from django.utils.translation import gettext as _
from course.models import Course
from volunteer.models.status import Status
from volunteer.models.state import State


class Volunteer(models.Model):
    first_name = models.CharField(max_length=200, verbose_name=_("نام"))
    last_name = models.CharField(max_length=300, verbose_name=_("نام خانوادگی"))
    email = models.EmailField(unique=True, verbose_name=_("ایمیل"))
    phone_number = models.CharField(max_length=11, verbose_name=_("نلفن"))
    year_of_birth = models.PositiveIntegerField(verbose_name=(_("سال تولد")))
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, limit_choices_to={"is_active": True},
                              related_name="volunteers", verbose_name=_("مرحله"))
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING,
                               limit_choices_to={"is_active": True}, verbose_name=_("وضعیت"))
    url_github = models.URLField(blank=True, null=True, verbose_name=_("آدرس گیت هاب"))
    url_linkedin = models.URLField(verbose_name=_("ادرس لینکدین"))
    register_time = models.DateTimeField(auto_now_add=True, verbose_name=_("زمان ثبت نام"))
    is_special = models.BooleanField(default=False, verbose_name=_("ویژه"))
    course = models.ManyToManyField(Course, through='CourseVolunteer', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

    class Meta:
        ordering = ("register_time",)
        verbose_name = "داوطلب"
        verbose_name_plural = "داوطلب ها"


class CourseVolunteer(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # You can add additional fields here if needed
