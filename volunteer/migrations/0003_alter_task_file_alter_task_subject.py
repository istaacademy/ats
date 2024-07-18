# Generated by Django 5.0.2 on 2024-07-16 14:43

import django.core.validators
import volunteer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0002_remove_volunteer_is_send_email_volunteer_is_special_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='file',
            field=models.FileField(null=True, upload_to=volunteer.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['rar', 'zip', 'pdf', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg', 'svg', 'SVG', 'xlsx'])], verbose_name='فایل'),
        ),
        migrations.AlterField(
            model_name='task',
            name='subject',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='موضوع'),
        ),
    ]