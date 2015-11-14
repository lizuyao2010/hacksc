# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_id', models.CharField(default=True, max_length=30)),
                ('course_name', models.CharField(default=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(default=True, max_length=30, serialize=False, primary_key=True)),
                ('first_name', models.CharField(default=True, max_length=30)),
                ('last_name', models.CharField(default=True, max_length=30)),
                ('gender', models.CharField(default=True, max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('year_in_school', models.CharField(default=True, max_length=2, choices=[(b'UN', b'UnderGraduate'), (b'GR', b'Graduate')])),
                ('major', models.CharField(default=True, max_length=20)),
            ],
        ),
    ]
