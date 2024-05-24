from django.db import models
from django.utils.translation import gettext as _
from course.models import Course


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
    first_name = models.CharField(max_length=200, verbose_name=_("First name"))
    last_name = models.CharField(max_length=300, verbose_name=_("Last name"))
    email = models.EmailField(unique=True, verbose_name=_("Email"))
    phone_number = models.CharField(max_length=11, verbose_name=_("Phone"))
    year_of_birth = models.PositiveIntegerField(verbose_name=(_("Year of birth")))
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, limit_choices_to={"is_active": True},
                              related_name="volunteers")
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING,
                               limit_choices_to={"is_active": True})
    url_github = models.URLField(blank=True, null=True, verbose_name=_("Url github"))
    url_linkedin = models.URLField(verbose_name=_("Url linkedin"))
    register_time = models.DateTimeField(auto_now_add=True, verbose_name=_("Register time"))
    is_send_email = models.BooleanField(default=False, verbose_name=_("Is send email"))
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
