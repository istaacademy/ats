# Generated by Django 5.0.2 on 2024-07-31 15:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calender', '0001_initial'),
        ('volunteer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='interviewee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='interviewee', to='volunteer.volunteer', verbose_name='مصاحبه شونده'),
        ),
        migrations.AddField(
            model_name='event',
            name='interviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='interviewer', to=settings.AUTH_USER_MODEL, verbose_name='مصاحبه کننده'),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='calender.time', verbose_name='زمان'),
        ),
    ]
