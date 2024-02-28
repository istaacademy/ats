from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "وضعیت "
        verbose_name_plural = "وضعیت ها"


class State(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300, blank=True, null=True)
    color = models.CharField(blank=True, null=True, max_length=200)

    class Meta:
        verbose_name = "موقعیت "
        verbose_name_plural = "موقعیت ها"

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    year_of_birth = models.PositiveIntegerField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name="volunteers")
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name="volunteers")
    url_github = models.URLField(blank=True, null=True)
    url_linkedin = models.URLField()
    register_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

    class Meta:
        ordering = ("register_time",)
        verbose_name = "داوطلب"
        verbose_name_plural = "داوطلب ها"
