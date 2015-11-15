# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(default=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='course_id',
            field=models.CharField(default=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='post_time',
            field=models.CharField(default=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='student_id',
            field=models.CharField(default=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(default=True, max_length=1024, null=True),
        ),
    ]
