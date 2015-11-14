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
                ('course_section', models.CharField(default=True, max_length=30)),
                ('course_type', models.CharField(default=True, max_length=2, choices=[(b'Le', b'Lecture'), (b'La', b'Lab'), (b'Q', b'Quiz')])),
                ('instructor', models.CharField(default=True, max_length=30)),
                ('location', models.CharField(default=True, max_length=30)),
                ('capcity', models.IntegerField(default=True)),
                ('registered', models.IntegerField(default=True)),
                ('start_time', models.TimeField(default=True)),
                ('end_time', models.TimeField(default=True)),
                ('days', models.CharField(default=True, max_length=30)),
                ('credits', models.FloatField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(default=True, max_length=30, serialize=False, primary_key=True)),
                ('first_name', models.CharField(default=True, max_length=30)),
                ('last_name', models.CharField(default=True, max_length=30)),
                ('gender', models.CharField(default=True, max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('year_in_school', models.CharField(default=True, max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior'), (b'GR', b'Graduate')])),
                ('major', models.CharField(default=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='polls.Student'),
        ),
    ]
