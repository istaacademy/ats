from django.db import models
from django.utils.translation import gettext as _
from course.models import Course
from django.core.validators import FileExtensionValidator
import datetime


def user_directory_path(instance, filename):
    date = datetime.datetime.now()
    return 'user_{0}/{1}{2}{3}-{4}'.format(instance.volunteer, date.year, date.strftime("%m"), date.strftime("%d"),
                                           filename)


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
