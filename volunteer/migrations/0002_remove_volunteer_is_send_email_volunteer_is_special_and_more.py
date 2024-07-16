# Generated by Django 5.0.2 on 2024-07-12 12:28

import django.core.validators
import django.db.models.deletion
import volunteer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='is_send_email',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='is_special',
            field=models.BooleanField(default=False, verbose_name='ویژه'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='last_name',
            field=models.CharField(max_length=300, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone_number',
            field=models.CharField(max_length=11, verbose_name='نلفن'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='register_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت نام'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='state',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='volunteers', to='volunteer.state', verbose_name='مرحله'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='status',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.DO_NOTHING, to='volunteer.status', verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='url_github',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس گیت هاب'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='url_linkedin',
            field=models.URLField(verbose_name='ادرس لینکدین'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='year_of_birth',
            field=models.PositiveIntegerField(verbose_name='سال تولد'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=300, verbose_name='موضوع')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال')),
                ('response_time', models.DateTimeField(blank=True, null=True, verbose_name='زمان پاسخ')),
                ('file', models.FileField(upload_to=volunteer.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['rar', 'zip', 'pdf', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg', 'svg', 'SVG', 'xlsx'])], verbose_name='فایل')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='volunteer.volunteer', verbose_name='داوطلب')),
            ],
            options={
                'verbose_name': 'تسک ها',
                'verbose_name_plural': 'تسک',
            },
        ),
    ]
