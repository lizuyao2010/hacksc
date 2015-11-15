# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_answer_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(default=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(default=True, max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(default=True, max_length=200, null=True),
        ),
    ]
