# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_student_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_id', models.CharField(default=True, max_length=30)),
                ('answerer_id', models.CharField(default=True, max_length=30)),
                ('question_id', models.CharField(default=True, max_length=30)),
                ('content', models.CharField(default=True, max_length=1024)),
                ('answer_time', models.TimeField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.CharField(default=True, max_length=30, serialize=False, primary_key=True)),
                ('course_id', models.CharField(default=True, max_length=30)),
                ('student_id', models.CharField(default=True, max_length=30)),
                ('title', models.CharField(default=True, max_length=1024)),
                ('post_time', models.TimeField(default=True)),
                ('content', models.CharField(default=True, max_length=1024)),
            ],
        ),
    ]
