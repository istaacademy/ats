# Generated by Django 5.0.2 on 2024-05-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام درس')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='زمان شروع')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='زمان پایان')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
            ],
        ),
    ]